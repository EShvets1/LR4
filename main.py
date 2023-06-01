from flask import Flask, render_template, request

app = Flask(__name__)   #Экземпляр приложения flask


@app.route('/') #Обозначение, что функция будет отвечать на веб запросы
@app.route('/index') #Обозначение, что функция будет отвечать за html файл
def index():
    return render_template("index.html")#Импорт html файла


@app.route('/', methods=['post', 'get']) #Обозначение, что функция будет отвечать на веб запросы с методами post и get
def form(): #функция form
    if request.method == 'POST': #если метод пост
        sum = int(request.form.get('num_1')) #сумма
        months = int(request.form.get('num_2')) #месяцы
        procent = int(request.form.get('num_3')) * 0.01 #процентная ставка
        type = request.form['options'] #Извлечение данных из запроса
    if type == '1':#Аннуитентный
        month_pay = round((sum * procent / 12 * pow((1 + procent / 12), months) / (pow((1 + procent / 12), months) - 1)), 2) #формула ежемесячного платежа
        all_pay = month_pay * 12 #формула общая суммы выплат
        all_procent = round((all_pay - sum), 2) #формула начисления процентов
        return render_template('index.html', ans= str("Ежемесячная выплата ≈ " + str(month_pay)), ans1= str("Общая сумма выплат ≈ " + str(all_pay)), ans2= str("Начисленные проценты ≈ " + str(all_procent) ) )
# вывод полученных результатов
    if type == '2':#Дифференцированный
        i = 0
        ans_template = str('')#пустая строчка
        all_pay = 0
        while i < months:
            ostatok = sum - sum / months * (i) #остаток
            procent_platezh = round(((ostatok * procent * 31)/ 365), 2) #процент
            month_pay = round((sum / months + procent_platezh), 2) #месячная выплата
            ans_template += str("выплата в " + str(i + 1) + "-м месяце ≈ " + str(month_pay) + ", ") # выплата в месяце
            all_pay += month_pay #прибавляем месячную плату к общей
            i += 1
        all_procent = round(all_pay - sum, 2) #начисленные проценты
        return render_template('index.html', ans= ans_template, ans1= str('Общая сумма выплат ≈ ' + str(all_pay)), ans2= str('Начисленные проценты ≈ ' + str(all_pay - sum)))
    elif type != '1': #если не выбран тип платежа
        return render_template('index.html', ans='Укажите тип платежа!')

if __name__ == '__main__':
    app.run()