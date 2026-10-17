"""
Grimório V2.0 - Oráculo Real & Diálogos do Rei Joaquim
Acolhimento, empatia, suporte emocional e tiragem de runas
"""

import random

FRASES_REI_ACOLHEDORAS = [
    "Mamãe Rainha, eu estou aqui cuidando do castelo para você descansar! Meu abraço de pequeno rei é o seu melhor escudo.",
    "Você é a rainha mais linda e corajosa de todos os reinos. Eu tenho tanto orgulho de você!",
    "Quando você sorri, o nosso castelo inteiro fica quentinho e cheio de luz. Toma um beijo real na sua testa!",
    "Não precisa se preocupar com nada agora, mamãe. Eu estou com a minha coroa firme e vigiando seus sonhos.",
    "Você cuida de todo mundo com tanto amor... agora senta aqui pertinho de mim e me dá um abraço bem apertado!",
    "Nós somos uma família invencível, mamãe! O papai e eu te amamos até as estrelas mais altas do infinito.",
    "Se o dia estiver cansativo, lembra que eu sou o seu guardião real para sempre. Eu te amo de montão!",
    "Respira fundo, minha rainha favorita! Você já fez coisas incríveis hoje e merece descansar como uma verdadeira soberana.",
    "Eu guardei um tesouro de carinho e risadinhas no meu coração só para te entregar hoje. Você é maravilhosa!",
    "Mamãe, você é a minha maior heroína. Não há tempestade no mundo que abale a nossa fortaleza de afeto.",
    "Tudo fica mais alegre e iluminado quando você entra no salão. Obrigado por ser a melhor rainha do mundo!",
    "Meu trono é pequenino, mas o meu amor e gratidão por você são maiores que todos os impérios da Terra."
]

RUNAS_DO_ORACULO = [
    {
        "nome": "Runa da Proteção (Algiz)",
        "simbolo": "ᛉ",
        "elemento": "Escudo de Éter",
        "mensagem": "Nenhum mal ou tempestade atinge quem caminha com o coração leal e puro. Seus limites são sagrados hoje."
    },
    {
        "nome": "Runa da Serenidade (Isa)",
        "simbolo": "ᛁ",
        "elemento": "Gelo Cristalino",
        "mensagem": "No silêncio e na pausa reside a mais pura sabedoria. Congele as preocupações e honre o seu momento presente."
    },
    {
        "nome": "Runa da Vitória (Sowilo)",
        "simbolo": "ᛋ",
        "elemento": "Sol Dourado",
        "mensagem": "A luz do triunfo já brilha sobre o teu caminho. Continue marchando, pois a vitória é o seu destino certo."
    },
    {
        "nome": "Runa da Clareza (Kenaz)",
        "simbolo": "ᚲ",
        "elemento": "Tocha da Revelação",
        "mensagem": "A névoa se dissipa diante da tua inteligência régia. Ideias brilhantes desabrocharão nas próximas horas."
    },
    {
        "nome": "Runa da Coragem (Tiwaz)",
        "simbolo": "ᛏ",
        "elemento": "Lâmina da Justiça",
        "mensagem": "Erga a tua cabeça. A justiça, a nobreza e a bravura correm em tuas veias. Enfrente o dia com ousadia."
    },
    {
        "nome": "Runa do Amor Real (Gebo)",
        "simbolo": "ᚷ",
        "elemento": "Aliança Eterna",
        "mensagem": "O amor e a cumplicidade são os maiores tesouros do império. Você é profundamente amada e valorizada."
    },
    {
        "nome": "Runa da Prosperidade (Fehu)",
        "simbolo": "ᚠ",
        "elemento": "Ouro das Montanhas",
        "mensagem": "A abundância flui para quem semeia com paciência e dedicação. Colheitas douradas se aproximam do teu reino."
    },
    {
        "nome": "Runa da Transformação (Dagaz)",
        "simbolo": "ᛞ",
        "elemento": "Alvorecer Celeste",
        "mensagem": "Um novo ciclo de realizações se inicia. Deixe para trás o que pesou ontem e receba o novo amanhecer."
    },
    {
        "nome": "Runa do Descanso Sagrado (Berkano)",
        "simbolo": "ᛒ",
        "elemento": "Floresta Mística",
        "mensagem": "Renove suas energias na serenidade da natureza. Cuidar de si mesma é governar com inteligência."
    },
    {
        "nome": "Runa da Intuição (Laguz)",
        "simbolo": "ᛚ",
        "elemento": "Águas Profundas",
        "mensagem": "Ouça a voz suave da tua alma. As respostas que você procura já habitam dentro do teu coração."
    },
    {
        "nome": "Runa da Força Interior (Uruz)",
        "simbolo": "ᚢ",
        "elemento": "Fogo Primordial",
        "mensagem": "Há uma potência inabalável dentro de você capaz de mover montanhas. Acredite na sua capacidade."
    },
    {
        "nome": "Runa da Alegria (Wunjo)",
        "simbolo": "ᚹ",
        "elemento": "Banquete das Estrelas",
        "mensagem": "Momentos de leveza, riso e deleite esperam por você. Permita-se saborear as doçuras da vida real."
    }
]

def gerar_resposta_rei(humor: str, desabafo: str) -> str:
    """Gera uma resposta empática, carinhosa e personalizada do Pequeno Rei Joaquim para a Rainha."""
    humor_lower = humor.lower()
    desabafo_lower = desabafo.lower()
    
    if "cansada" in humor_lower or "sobrecarregada" in humor_lower or "exaust" in desabafo_lower or "dormir" in desabafo_lower:
        return (
            "Mamãe Rainha, deita um pouquinho no meu colo e fecha os olhos. "
            "Eu já fechei as cortinas do castelo e dei ordem para os soldadinhos fazerem silêncio total. "
            "Você batalhou muito hoje e merece o descanso mais quentinho do mundo. Eu cuido de tudo agora!"
        )
    elif "ansiosa" in humor_lower or "medo" in desabafo_lower or "nervosa" in desabafo_lower or "preocupad" in desabafo_lower:
        return (
            "Segura a minha mãozinha, mamãe! Olha para mim: nós somos uma família corajosa e invencível. "
            "Respira bem devagarinho comigo... 1, 2, 3... solta o ar. Vai dar tudo certo, o meu cetro e o meu amor estão te protegendo!"
        )
    elif "triste" in humor_lower or "choro" in desabafo_lower or "dói" in desabafo_lower or "machuc" in desabafo_lower:
        return (
            "Não chora, minha rainha linda... Toma meu abraço mais apertado e um beijinho de cura na sua bochecha. "
            "Se o mundo lá fora pesou, aqui dentro você tem um príncipe guardião que te ama mais que tudo nessa vida. Estou com você sempre!"
        )
    elif "radiante" in humor_lower or "feliz" in humor_lower or "vitoriosa" in desabafo_lower or "consegui" in desabafo_lower:
        return (
            "Ebaaa! A minha mamãe é a maior campeã de todo o reino! Teu sorriso deixa a Sala do Trono brilhando como ouro puro! "
            "Vou colocar a minha melhor coroa e comemorar com você comendo os doces mais gostosos da corte real!"
        )
    elif "tranquila" in humor_lower or "serena" in humor_lower or "paz" in desabafo_lower:
        return (
            "Que delícia ver você serena e em paz, mamãe. Quando você está calma, o nosso castelo fica parecendo um jardim em flor. "
            "É tão bom estar pertinho de você governando os nossos dias felizes!"
        )
    else:
        conselhos = [
            "Mamãe Rainha, ouvi tudinho com o coração aberto. Minha coroinha brilha de orgulho por você todos os dias. Eu te amo muito!",
            "Não importa o que aconteça lá fora, o nosso abraço é a fortaleza mais impenetrável de todo o reino. Conta comigo sempre!",
            "Você é a rainha mais especial do universo e a mamãe mais doce do mundo. Toma um beijo real bem quentinho!"
        ]
        return random.choice(conselhos)


def sortear_runa() -> dict:
    """Tira uma runa aleatória do oráculo."""
    return random.choice(RUNAS_DO_ORACULO)
