import asyncio
import logging

from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import other_handlers, user_handlers

#Логгер
logger = logging.getLogger(__name__)

#конфігурація і запуск бота
async def main():
    #конфігуруєм логування
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s '
               u'[%(asctime)s] - %(name)s - %(message)s')

    #повідомленя про запуск бота
    logger.info('Startying bot')

    config: Config = load_config()

    bot: Bot = Bot(token=config.tg_bot.token,
                   parse_mode='HTML')
    dp: Dispatcher = Dispatcher()

    # Реєструєм роутери в діспатчері
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    # Пропускаєм минулі апдейты та запускаєм polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        #запускаєм main в асінх режимі
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        #Повідомленя про помилку
        #KeyboardInterrupt чи SystemExit
        logger.error('Bot stopped!')



