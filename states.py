from aiogram.fsm.state import State, StatesGroup

class OrderState(StatesGroup):
    entering_car_num = State() # Mashina raqamini kutish
    entering_time = State()    # Kelish vaqtini kutish