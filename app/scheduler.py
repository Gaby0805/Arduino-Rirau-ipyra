import logging
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from datetime import datetime
from app.core.database import SessionLocal
from app.models import Alarms
from app.api.routes.socket import activate_socket
from pytz import timezone
# Configuração básica de logs
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
tz_ms = timezone("America/Campo_Grande")
scheduler = AsyncIOScheduler()


async def trigger_alarm(alarm_id: int):
    """Função executada quando o alarme dispara."""
    logging.info(f"⏰ Disparando alarme ID={alarm_id} no horário {datetime.now()}")
    await activate_socket("ALARME")


def load_alarms():
    """Carrega os alarmes ativos do banco e agenda no APScheduler para disparo no horário correto."""
    logging.info("🔄 Iniciando carregamento de alarmes ativos...")

    try:
        with SessionLocal() as session:
            logging.info("📂 Sessão com o banco iniciada.")

            stmt = (
                select(Alarms)
                .where(Alarms.is_active == True)
                .options(selectinload(Alarms.days))
            )

            logging.info("📜 Executando consulta para buscar alarmes ativos...")
            result = session.execute(stmt)

            alarms = result.scalars().all()
            logging.info(f"📦 {len(alarms)} alarmes encontrados.")

            if not alarms:
                logging.warning("⚠️ Nenhum alarme ativo encontrado no banco.")
                return

            for alarm in alarms:
                logging.info(f"📌 Processando alarme ID={alarm.id} ({alarm.label}) - Hora: {alarm.time}")

                if not alarm.days:
                    logging.warning(f"⚠️ Alarme ID={alarm.id} não possui dias configurados.")
                    continue

                for day in alarm.days:
                    # Agendamento para disparar no horário exato do alarme
                    scheduler.add_job(
                        trigger_alarm,
                        'cron',
                        day_of_week=day.day_of_week,  # 0=Domingo ... 6=Sábado
                        hour=alarm.time.hour,
                        minute=alarm.time.minute,
                        args=[alarm.id]
                    )
                    logging.info(
                        f"✅ Alarme ID={alarm.id} ({alarm.label}) agendado para dia {day.day_of_week} às {alarm.time}"
                    )

        logging.info("🎯 Carregamento e agendamento de alarmes concluído com sucesso.")

    except Exception as e:
        logging.error(f"❌ Erro ao carregar ou agendar alarmes: {e}", exc_info=True)
