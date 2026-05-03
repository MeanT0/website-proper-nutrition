def calculate_bmi(weight: float, height_cm: float) -> str:
    """Расчёт индекса массы тела (ИМТ)"""
    if weight <= 0 or height_cm <= 0:
        return "Введите корректные данные"

    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)

    if bmi < 18.5:
        category = "Дефицит массы тела"
    elif bmi < 25:
        category = "Норма"
    elif bmi < 30:
        category = "Избыточная масса тела"
    else:
        category = "Ожирение"

    return f"{bmi:.1f} ({category})"


def calculate_tdee(sex: str, age: float, weight: float, height_cm: float, activity: float) -> str:
    """Расчёт суточной нормы калорий (формула Миффлина-Сан Жеора)"""
    if age <= 0 or weight <= 0 or height_cm <= 0:
        return "Введите корректные данные"

    # Базовый метаболизм (BMR)
    if sex == "male":
        bmr = (10 * weight) + (6.25 * height_cm) - (5 * age) + 5
    else:
        bmr = (10 * weight) + (6.25 * height_cm) - (5 * age) - 161

    tdee = bmr * activity
    return f"{int(tdee)} ккал/день"