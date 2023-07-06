import utils
import read_csv
import charts
import pandas as pd
# la librería pandas es muy util para leer, filtrar y trabajar archivos csv


def run():
    '''
    data = list(filter(lambda item: item['Continent'] == 'South America', data))

    countries = list(map(lambda x: x['Country/Territory'], data))
    percentages = list(map(lambda x: x['World Population Percentage'], data))
    '''
    # dataframe, generalmente df, son todos los datos de donde vamos a obtener la información
    df = pd.read_csv('data.csv') # read_csv es un metodo de panda no la función que construimos antes para leer el csv y contruir un diccionario
    df = df[df['Continent'] == 'Africa'] # vamos al dataframe para seleccionar los datos de la columna (Continent) que sea iguales a (Africa). Esta línea es para filtrar, entrega el mismo resultado de la función que creamos con list+filter+lambda
    
    countries = df['Country/Territory'].values # la función de pandas que nos permite tener los valores de una columna, mismo resultado de la línea en la que usamos list+map+lambda 
    percentages = df['World Population Percentage'].values
    charts.generate_pie_chart(countries,  percentages)
    
    data = read_csv.read_csv('data.csv')
    country = input('Type Country => ')
    print(country)

    result = utils.population_by_country(data, country)

    if len(result) > 0:
        country = result[0]
        print(country)
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(country['Country/Territory'], labels, values)


if __name__ == '__main__':
    run()
