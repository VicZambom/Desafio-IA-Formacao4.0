import pickle

with open('melhor_modelo.pkl', 'rb') as f:
    modelo_carregado = pickle.load(f)

X_novos_dados = [[5, 116, 74, 0, 0, 25.6, 0.201, 30]] 

resultado = modelo_carregado.predict(X_novos_dados)

print("Predição:", resultado)
