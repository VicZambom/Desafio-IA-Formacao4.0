import pickle
import gradio as gr

with open('melhor_modelo.pkl', 'rb') as f:
    modelo_carregado = pickle.load(f)

def predizer_diabetes(pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age):
    dados = [[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]]
    resultado = modelo_carregado.predict(dados)[0]
    if resultado == 0:
        return "Sem diabetes"
    else:
        return "Com diabetes"

# Criando a interface com Gradio
interface = gr.Interface(
    fn=predizer_diabetes,
    inputs=[
        gr.Number(label="Número de gestações"),
        gr.Number(label="Nível de glicose"),
        gr.Number(label="Pressão arterial"),
        gr.Number(label="Espessura da pele"),
        gr.Number(label="Insulina"),
        gr.Number(label="IMC"),
        gr.Number(label="Função pedigree de diabetes"),
        gr.Number(label="Idade")
    ],
    outputs="text",
    title="Predição de Diabetes - Pima Indians Dataset",
    description="Informe os dados para saber se a pessoa tem diabetes ou não."
)

interface.launch(share=True)

