from bokeh.plotting import figure, output_file, show 

if __name__ == "__main__":
    output_file('graficado.html')

    fig = figure()

    total = int(input('Cuantos valores quieres graficar? '))

    x = list(range(total))

    y = []

    for i in x:
        val = int(input(f'Valor y para {x[i]} '))
        y.append(val)

    fig.line(x, y, line_width=2)
    
    show(fig)