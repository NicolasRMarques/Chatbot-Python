#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random
from datetime import datetime


# In[6]:


#Desafio

comandos = ["MUDAR NOME DO BOT", "TOM DA MENSAGEM", "AJUDA"]
comandos = [comando.strip().upper() for comando in comandos]
ajuda = ["Converse comigo que eu te respondo", "Mesmo se eu não souber, eu posso aprender :)"]
historico = []
nomeBot = "Bot"

def setNomeBot(nome):
    global nomeBot 
    nomeBot = nome
    
def getNomeBot():
    global nomeBot
    return nomeBot

def executaComando_GUI(nome):
    mensagem = ""
    if nome == comandos[0]:
        #desenvolvimento
        mensagem = nomeBot + ": Digite um novo nome\n"
    elif nome == comandos[1]:
        #debug
        print(getHistorico())
        print("Mensagem analisada: ",getUltimaMensagem())
        mensagem = nomeBot + ": " + analisaTom(getUltimaMensagem()) + "\n"
    elif nome == comandos[2]:
        i = 1
        mensagem = nomeBot + ":\n"
        for a in ajuda:
            mensagem = mensagem + a + "\n"
        mensagem = mensagem + "Lista de Comandos:\n"
        for c in comandos:
            mensagem = mensagem + str(i) + "- " + c + "\n"
            i+=1
    return mensagem

def getHistorico():
    global historico
    return historico

def setHistorico(texto):
    historico.append(texto)

def getUltimaMensagem():
    if getHistorico():
        return getHistorico()[-2]
    else:
        return ""

def analisaTom(texto):
    texto=texto.lower()
    lista_reclamacao = ["ruim", "péssimo", "horrível", "terrível", "insuportável", "lento", "caro", "demorado", "frustrante", "inaceitável"]
    lista_elogio = ["bom", "ótimo", "excelente", "maravilhoso", "fantástico", "rápido", "barato", "eficiente", "satisfatório", "perfeito"]
    lista_sugestao = ["sugiro", "recomendo", "proponho", "aconselho", "indico", "melhorar", "adicionar", "remover", "alterar", "considerar"]
    lista_dialogo = ["olá", "oi", "bom dia", "boa tarde", "boa noite", "como vai", "tudo bem", "obrigado", "por favor", "desculpe"]
    
    reclamacaoCount = 0
    elogioCount = 0
    sugestaoCount = 0
    dialogoCount = 0
    
    for palavra in texto.split():
        if palavra in lista_reclamacao:
            reclamacaoCount += 1
        if palavra in lista_elogio:
            elogioCount += 1
        if palavra in lista_sugestao:
            sugestaoCount += 1
        if palavra in lista_dialogo:
            dialogoCount += 1
    
    counts = {
        "Reclamação": reclamacaoCount,
        "Elogio": elogioCount,
        "Sugestão": sugestaoCount,
        "Diálogo": dialogoCount
    }

    if all(value == 0 for value in counts.values()):
        return "Neutro"
    
    max_count = max(counts, key=counts.get)
    return max_count

def salva_sugestao(sugestao):
    with open("baseDeConhecimento.txt", "a+") as conhecimento:
        conhecimento.write("Chatbot: " + sugestao)
    
# In[1]:
  
def saudacao_GUI():
    global nomeBot 
    nome = nomeBot
    
    #Desafio
    
    agora = datetime.now()
    hora = agora.hour

    if 6 <= hora <= 12:
        saudacao = "Bom dia!"
    elif 12 < hora < 18:
        saudacao = "Boa tarde!"
    else:
        saudacao = "Boa noite!"

    frases = [f"{saudacao} Meu nome é " + nome + ". Como vai você?\n"]
    return frases[0]
    #print(frases[random.randint(0,2)])


# In[12]:


# In[7]:
            
def buscaResposta_GUI(texto):
    global nomeBot 
    nome = nomeBot
    global historico
    historico.append(texto)
    texto_upper = texto.replace("Cliente: ", "").strip().upper()
    if texto_upper in comandos:
        return executaComando_GUI(texto_upper)
    with open("baseDeConhecimento.txt", "a+") as conhecimento:
        conhecimento.seek(0)
        while True:
            viu = conhecimento.readline()
            if viu != "":
                viu_upper = viu.upper()
                if jaccard(texto_upper, viu_upper) > 0.3:
                    proximalinha = conhecimento.readline()
                    if "Chatbot: " in proximalinha:
                        return proximalinha
            else:
                conhecimento.write("\nCliente: " + texto_upper + "\n")
                return "Me desculpe, não sei o que falar"
            
def jaccard(textoUsuario, textoBase):
    textoUsuario = limpa_frase(textoUsuario)
    textoBase = limpa_frase(textoBase)
    if len(textoBase) < 1:
        return 0
    else:
        palavras_em_comum = 0
        for palavra in textoUsuario.split():
            if palavra in textoBase.split():
                palavras_em_comum += 1
        return palavras_em_comum / (len(textoBase.split()))

def limpa_frase(frase):
    tirar = ["?", "!", "...", ".", ",", "Cliente: ", "\n"]
    for t in tirar:
        frase = frase.replace(t, "")
    frase = frase.upper()
    return frase

# In[14]:

def exibeResposta_GUI(texto, resposta):
    global nomeBot
    return resposta.replace("Chatbot", nomeBot)

