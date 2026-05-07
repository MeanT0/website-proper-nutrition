from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def calc(request):


    # Результаты
    bmi_result = None
    tdee_result = None
    bju_result = None

    # Сохраняем введённые значения
    form_data = {}

    if request.method == 'POST':
        # Калькулятор ИМТ
        if 'calc_bmi' in request.POST:
            height = float(request.POST.get('bmi_height', 0))
            weight = float(request.POST.get('bmi_weight', 0))

            if height > 0 and weight > 0:
                height_m = height / 100
                bmi = weight / (height_m ** 2)

                if bmi < 18.5:
                    category = "Дефицит массы"
                    category_class = "underweight"
                elif bmi < 25:
                    category = "Норма"
                    category_class = "normal"
                elif bmi < 30:
                    category = "Избыток"
                    category_class = "overweight"
                else:
                    category = "Ожирение"
                    category_class = "obese"

                bmi_result = {
                    'value': f"{bmi:.1f}",
                    'category': category,
                    'category_class': category_class
                }

                form_data['bmi_height'] = request.POST.get('bmi_height')
                form_data['bmi_weight'] = request.POST.get('bmi_weight')

        # Калькулятор калорий (TDEE)
        elif 'calc_tdee' in request.POST:
            sex = request.POST.get('tdee_sex', 'male')
            age = float(request.POST.get('tdee_age', 0))
            height = float(request.POST.get('tdee_height', 0))
            weight = float(request.POST.get('tdee_weight', 0))
            activity = float(request.POST.get('tdee_activity', 1.2))

            if age > 0 and height > 0 and weight > 0:
                # Формула Миффлина-Сан Жеора
                if sex == 'male':
                    bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
                else:
                    bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161

                tdee = bmr * activity

                tdee_result = {
                    'calories': f"{int(tdee)}",
                    'lose': f"{int(tdee * 0.8)}",
                    'maintain': f"{int(tdee)}",
                    'gain': f"{int(tdee * 1.15)}"
                }

                form_data['tdee_sex'] = sex
                form_data['tdee_age'] = request.POST.get('tdee_age')
                form_data['tdee_height'] = request.POST.get('tdee_height')
                form_data['tdee_weight'] = request.POST.get('tdee_weight')
                form_data['tdee_activity'] = request.POST.get('tdee_activity')

        # Калькулятор БЖУ
        elif 'calc_bju' in request.POST:
            weight = float(request.POST.get('bju_weight', 0))
            calories = float(request.POST.get('bju_calories', 0))
            goal = request.POST.get('bju_goal', 'balance')

            if weight > 0 and calories > 0:
                # На основе данных из документа (г/кг веса тела)
                if goal == 'lose':
                    protein_g_per_kg = 2.0
                    fat_g_per_kg = 0.8
                elif goal == 'gain':
                    protein_g_per_kg = 2.0
                    fat_g_per_kg = 1.0
                else:
                    protein_g_per_kg = 1.6
                    fat_g_per_kg = 1.0

                # Рассчитываем белки и жиры в граммах
                protein_grams = int(weight * protein_g_per_kg)
                fat_grams = int(weight * fat_g_per_kg)

                # Калории от белков и жиров
                protein_cal = protein_grams * 4
                fat_cal = fat_grams * 9

                # Углеводы забирают остаток калорий
                remaining_calories = calories - (protein_cal + fat_cal)
                if remaining_calories > 0:
                    carbs_grams = int(remaining_calories / 4)
                else:
                    carbs_grams = 0

                # Проверяем соответствие процентам
                protein_percent = (protein_cal / calories) * 100
                fat_percent = (fat_cal / calories) * 100
                carbs_percent = (carbs_grams * 4 / calories) * 100

                bju_result = {
                    'protein_grams': protein_grams,
                    'protein_cal': protein_cal,
                    'protein_percent': protein_percent,
                    'fat_grams': fat_grams,
                    'fat_cal': fat_cal,
                    'fat_percent': fat_percent,
                    'carbs_grams': carbs_grams,
                    'carbs_cal': carbs_grams * 4,
                    'carbs_percent': carbs_percent,
                    'total_cal': calories
                }

                form_data['bju_weight'] = request.POST.get('bju_weight')
                form_data['bju_calories'] = request.POST.get('bju_calories')
                form_data['bju_goal'] = goal

    context = {
        'title': 'Калькуляторы питания',
        'bmi_result': bmi_result,
        'tdee_result': tdee_result,
        'bju_result': bju_result,
        **form_data
    }

    return render(request, 'main/calc.html', context)