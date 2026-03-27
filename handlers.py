from aiogram import Router, F, types, Bot
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from config import SERVICES, ADMIN_ID
import keyboards as kb
from states import OrderState

router = Router()


@router.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("🚗 Avto-servis botina xosh kelibsiz!\nXizmetlerdi ko'riw ushin /xizmetler buyrug'in basin'.")


@router.message(Command("xizmetler"))
async def show_services(message: types.Message):
    await message.answer("🛠 Xizmet turin saylan':", reply_markup=kb.get_services_kb())


@router.callback_query(F.data.startswith("ser_"))
async def service_selected(callback: types.CallbackQuery, state: FSMContext):
    service_id = callback.data.split("_")[1]
    service_name = SERVICES[service_id][0]
    await state.update_data(selected_service=service_name)
    await callback.message.edit_text(f"✅ Saylandi: {service_name}\n\n🚗 Mashina nomerin jazin':")
    await state.set_state(OrderState.entering_car_num)


@router.message(OrderState.entering_car_num)
async def car_num_step(message: types.Message, state: FSMContext):
    await state.update_data(car_num=message.text)
    await message.answer("🕒 Qaysi waqitqa kelesiz? (maselen: Bugin 18:00):")
    await state.set_state(OrderState.entering_time)


@router.message(OrderState.entering_time)
async def final_step(message: types.Message, state: FSMContext, bot: Bot):
    await state.update_data(arrival_time=message.text)
    data = await state.get_data()

    order_text = (
        "🔔 JAN'A BUYIRTPA!**\n\n"
        f"🛠 **Xizmet: {data['selected_service']}\n"
        f"🚗 Mashina: {data['car_num']}\n"
        f"🕒 Waqit: {data['arrival_time']}\n"
        f"👤 Klient: @{message.from_user.username or 'Link yoq'}"
    )

    await bot.send_message(chat_id=ADMIN_ID, text=order_text, parse_mode="Markdown")
    await message.answer("✅ Rahmet! Buyirtpan'iz adminge jiberildi.")
    await state.clear()