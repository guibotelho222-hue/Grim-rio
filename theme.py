"""
Grimório V2.0 - Dark Fantasy Modern Theme & Engine de Temas
Paletas dinâmicas, cálculo de fase lunar e influência mística, compatibilidade Flet 1.0 e estilos globais
"""

import sys
import os
from datetime import datetime
import flet as ft

def resolve_path(relative_path: str) -> str:
    """Resolve caminhos absolutos em modo Dev, Executável PyInstaller (_MEIPASS) e Pacote Mobile."""
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir, relative_path)

# Compatibilidade e Engine de Áudio Síncrona
try:
    import winsound
except ImportError:
    winsound = None

class FletAudioCompat(ft.Container):
    """Controle de Áudio Síncrono compatível com Flet e Windows."""
    def __init__(self, src: str, autoplay: bool = False, volume: float = 1.0):
        super().__init__(visible=False, width=0, height=0)
        self.src = src
        self.autoplay = autoplay
        self.volume = volume
        if autoplay:
            self.play()

    def play(self):
        try:
            caminho = self.src
            if caminho.endswith(".mp3"):
                caminho_wav = caminho[:-4] + ".wav"
                if os.path.exists(caminho_wav):
                    caminho = caminho_wav
            if os.path.exists(caminho) and winsound:
                winsound.PlaySound(caminho, winsound.SND_FILENAME | winsound.SND_ASYNC)
            elif winsound:
                winsound.MessageBeep(winsound.MB_ICONASTERISK)
        except Exception as e:
            print(f"[Audio] Erro ao reproduzir {self.src}: {e}")

    def release(self):
        pass

if not hasattr(ft, "Audio"):
    ft.Audio = FletAudioCompat

def disparar_notificacao_sistema(titulo: str, mensagem: str, app_icon: str = None) -> bool:
    """Dispara notificação de sistema nativa (Windows Toast) utilizando plyer."""
    try:
        from plyer import notification
        icone = app_icon if (app_icon and os.path.exists(app_icon)) else resolve_path("assets/logo.ico")
        notification.notify(
            title=titulo,
            message=mensagem,
            app_name="Grimório",
            app_icon=icone if os.path.exists(icone) else None,
            timeout=5
        )
        return True
    except Exception as e:
        print(f"[Notificação] plyer: {e}")
        return False


# Paletas Pré-definidas do Grimório
TEMAS = {
    "Dark Fantasy Dourado": {
        "bg_dark": "#121214",
        "bg_surface": "#181820",
        "bg_card": "#21212D",
        "bg_card_light": "#2A2A3B",
        "bg_input": "#16161E",
        "primary": "#D4AF37",
        "light": "#FFD700",
        "secondary": "#8B5CF6",
        "secondary_light": "#A78BFA",
        "container": "#2E2612",
        "border_color": "#D4AF37",
        "border_subtle": "#3D3418",
        "text_primary": "#F8FAFC",
        "text_secondary": "#94A3B8",
        "text_muted": "#64748B"
    },
    "Roxo Arcano": {
        "bg_dark": "#0D0915",
        "bg_surface": "#150F24",
        "bg_card": "#1E1633",
        "bg_card_light": "#281E44",
        "bg_input": "#130E20",
        "primary": "#A855F7",
        "light": "#C084FC",
        "secondary": "#E879F9",
        "secondary_light": "#F0ABFC",
        "container": "#291340",
        "border_color": "#A855F7",
        "border_subtle": "#581C87",
        "text_primary": "#FAF5FF",
        "text_secondary": "#D8B4FE",
        "text_muted": "#7E22CE"
    },
    "Esmeralda Obscura": {
        "bg_dark": "#0B1411",
        "bg_surface": "#0F1E19",
        "bg_card": "#152C25",
        "bg_card_light": "#1C3A31",
        "bg_input": "#0D1814",
        "primary": "#10B981",
        "light": "#34D399",
        "secondary": "#059669",
        "secondary_light": "#6EE7B7",
        "container": "#063323",
        "border_color": "#10B981",
        "border_subtle": "#065F46",
        "text_primary": "#F0FDF4",
        "text_secondary": "#A7F3D0",
        "text_muted": "#047857"
    },
    "Chumbo Sóbrio": {
        "bg_dark": "#0F1115",
        "bg_surface": "#161920",
        "bg_card": "#1F232D",
        "bg_card_light": "#282E3B",
        "bg_input": "#14171E",
        "primary": "#94A3B8",
        "light": "#E2E8F0",
        "secondary": "#64748B",
        "secondary_light": "#CBD5E1",
        "container": "#1E293B",
        "border_color": "#94A3B8",
        "border_subtle": "#334155",
        "text_primary": "#F8FAFC",
        "text_secondary": "#94A3B8",
        "text_muted": "#64748B"
    }
}

# Funções de Compatibilidade Flet 1.0+ e Legado
def border_all(width: float = 1, color: str = "#3D3418") -> ft.Border:
    if hasattr(ft, "Border") and hasattr(ft.Border, "all"):
        return ft.Border.all(width=width, color=color)
    return ft.border.all(width, color)

def border_only(**kwargs) -> ft.Border:
    if hasattr(ft, "Border") and hasattr(ft.Border, "only"):
        return ft.Border.only(**kwargs)
    return ft.border.only(**kwargs)

def border_radius_all(radius: float) -> ft.BorderRadius:
    if hasattr(ft, "BorderRadius") and hasattr(ft.BorderRadius, "all"):
        return ft.BorderRadius.all(radius)
    return ft.border_radius.all(radius)

def border_radius_only(**kwargs) -> ft.BorderRadius:
    if hasattr(ft, "BorderRadius") and hasattr(ft.BorderRadius, "only"):
        return ft.BorderRadius.only(**kwargs)
    return ft.border_radius.only(**kwargs)

def padding_all(pad: float) -> ft.Padding:
    if hasattr(ft, "Padding") and hasattr(ft.Padding, "all"):
        return ft.Padding.all(pad)
    return ft.padding.all(pad)

def padding_symmetric(horizontal: float = 0, vertical: float = 0) -> ft.Padding:
    if hasattr(ft, "Padding") and hasattr(ft.Padding, "symmetric"):
        return ft.Padding.symmetric(horizontal=horizontal, vertical=vertical)
    return ft.padding.symmetric(horizontal=horizontal, vertical=vertical)

def padding_only(left: float = 0, top: float = 0, right: float = 0, bottom: float = 0) -> ft.Padding:
    if hasattr(ft, "Padding") and hasattr(ft.Padding, "only"):
        return ft.Padding.only(left=left, top=top, right=right, bottom=bottom)
    return ft.padding.only(left=left, top=top, right=right, bottom=bottom)

def icon_nobre(icone_data, size=None, color=None) -> ft.Icon:
    kwargs = {}
    if size is not None:
        kwargs["size"] = size
    if color is not None:
        kwargs["color"] = color
    return ft.Icon(icone_data, **kwargs)

# Paleta Ativa Global
TEMA_ATIVO = "Dark Fantasy Dourado"
TEMA_PADRAO = TEMAS[TEMA_ATIVO]
BG_DARK = TEMA_PADRAO["bg_dark"]
BG_SURFACE = TEMA_PADRAO["bg_surface"]
BG_CARD = TEMA_PADRAO["bg_card"]
BG_CARD_LIGHT = TEMA_PADRAO["bg_card_light"]
BG_INPUT = TEMA_PADRAO["bg_input"]

GOLD_PRIMARY = TEMA_PADRAO["primary"]
GOLD_LIGHT = TEMA_PADRAO["light"]
GOLD_MUTED = "#9A8132"
GOLD_CONTAINER = TEMA_PADRAO["container"]

PURPLE_PRIMARY = TEMA_PADRAO["secondary"]
PURPLE_LIGHT = TEMA_PADRAO["secondary_light"]
PURPLE_DARK = "#4C1D95"
PURPLE_CONTAINER = "#261B40"

BORDER_GOLD = border_all(1, TEMA_PADRAO["border_color"])
BORDER_PURPLE = border_all(1, TEMA_PADRAO["secondary"])
BORDER_SUBTLE = border_all(1, TEMA_PADRAO["border_subtle"])

TEXT_PRIMARY = "#F8FAFC"
TEXT_SECONDARY = "#94A3B8"
TEXT_MUTED = "#64748B"
SUCCESS_GREEN = "#10B981"
DANGER_RED = "#EF4444"
MANA_BLUE = "#38BDF8"
HP_RED = "#F43F5E"

BORDER_RADIUS = 12

def get_theme_colors(nome_tema: str = "Dark Fantasy Dourado") -> dict:
    return TEMAS.get(nome_tema, TEMAS["Dark Fantasy Dourado"])

def aplicar_tema(nome_tema: str):
    """Atualiza as variáveis globais de cor de theme.py para recoloração instantânea."""
    global TEMA_ATIVO, BG_DARK, BG_SURFACE, BG_CARD, BG_CARD_LIGHT, BG_INPUT
    global GOLD_PRIMARY, GOLD_LIGHT, GOLD_CONTAINER, BORDER_GOLD
    global PURPLE_PRIMARY, PURPLE_LIGHT, PURPLE_CONTAINER, BORDER_PURPLE, BORDER_SUBTLE
    global TEXT_PRIMARY, TEXT_SECONDARY, TEXT_MUTED

    cores = get_theme_colors(nome_tema)
    TEMA_ATIVO = nome_tema
    BG_DARK = cores["bg_dark"]
    BG_SURFACE = cores["bg_surface"]
    BG_CARD = cores["bg_card"]
    BG_CARD_LIGHT = cores["bg_card_light"]
    BG_INPUT = cores["bg_input"]

    GOLD_PRIMARY = cores["primary"]
    GOLD_LIGHT = cores["light"]
    GOLD_CONTAINER = cores["container"]

    PURPLE_PRIMARY = cores["secondary"]
    PURPLE_LIGHT = cores["secondary_light"]
    PURPLE_CONTAINER = cores["container"]

    BORDER_GOLD = border_all(1, cores["border_color"])
    BORDER_PURPLE = border_all(1, cores["secondary"])
    BORDER_SUBTLE = border_all(1, cores["border_subtle"])

    TEXT_PRIMARY = cores.get("text_primary", "#F8FAFC")
    TEXT_SECONDARY = cores.get("text_secondary", "#94A3B8")
    TEXT_MUTED = cores.get("text_muted", "#64748B")

def botao_preenchido(
    texto: str,
    on_click=None,
    bgcolor: str = None,
    color: str = "#121214",
    icon=None
) -> ft.Control:
    if bgcolor is None:
        bgcolor = GOLD_PRIMARY
        
    kwargs = {
        "on_click": on_click,
        "bgcolor": bgcolor,
        "color": color
    }
    if icon:
        kwargs["icon"] = icon
        
    if hasattr(ft, "FilledButton"):
        return ft.FilledButton(texto, **kwargs)
    elif hasattr(ft, "ElevatedButton"):
        return getattr(ft, "ElevatedButton")(texto, **kwargs)
    return ft.Container(
        content=ft.Text(texto, color=color, weight=ft.FontWeight.BOLD),
        bgcolor=bgcolor,
        on_click=on_click,
        padding=padding_symmetric(horizontal=16, vertical=8),
        border_radius=border_radius_all(8)
    )

def get_dark_theme(nome_tema: str = "Dark Fantasy Dourado") -> ft.Theme:
    cores = get_theme_colors(nome_tema)
    try:
        return ft.Theme(
            color_scheme=ft.ColorScheme(
                surface=cores["bg_surface"],
                primary=cores["primary"],
                secondary=cores["secondary"],
                on_surface=cores.get("text_primary", TEXT_PRIMARY),
            )
        )
    except Exception:
        return ft.Theme()

# ==================== CÁLCULO E INFLUÊNCIA LUNAR ====================
def calcular_fase_lua(dt: datetime = None) -> tuple:
    """Retorna (nome_fase, emoji_lua) com base na órbita sinódica lunar (29.53 dias)."""
    if dt is None:
        dt = datetime.now()
    ref = datetime(2000, 1, 6, 18, 14)
    diff = (dt - ref).total_seconds() / 86400.0
    dias = diff % 29.53058867
    
    fases = [
        (1.84, "Lua Nova", "🌑"),
        (5.53, "Crescente", "🌒"),
        (9.22, "Quarto Crescente", "🌓"),
        (12.91, "Gibosa Crescente", "🌔"),
        (16.61, "Lua Cheia", "🌕"),
        (20.30, "Gibosa Minguante", "🌖"),
        (23.99, "Quarto Minguante", "🌗"),
        (27.69, "Minguante", "🌘"),
    ]
    for lim, nome, emoji in fases:
        if dias < lim:
            return nome, emoji
    return "Lua Nova", "🌑"

DADOS_INFLUENCIA_LUNAR = {
    "Lua Nova": {
        "influencia": "Momento sagrado de renovação e recolhimento místico. Os céus silenciam para que a mente da Rainha conceba novas aspirações. A energia favorece a clareza interior, novos começos e a formulação de planos sem o peso do passado.",
        "orientacao": "Plante intenções com paciência. Defina as grandes Quests do ciclo, organize seus pensamentos e guarde energia para os dias de ação intensa."
    },
    "Crescente": {
        "influencia": "A foice de prata ergue-se nas trevas trazendo impulso criativo e ânimo heroico. A clareza transforma-se em vigor; os primeiros passos dos projetos ganham a bênção da expansão e da vitalidade.",
        "orientacao": "Dê início prático às missões pendentes. Pequenos hábitos mantidos hoje germinarão como muralhas impenetráveis nos próximos ciclos."
    },
    "Quarto Crescente": {
        "influencia": "Equilíbrio entre luz e sombra, teste de firmeza e comando régio. As forças arcanas demandam decisão resoluta e coragem para transpor obstáculos que tentam minar o foco da corte.",
        "orientacao": "Mantenha o foco inabalável. Elimine distrações da corte, resolva dúvidas pendentes e não hesite diante de tarefas exigentes."
    },
    "Gibosa Crescente": {
        "influencia": "A maré de poder ascende em direção ao ápice. O intelecto brilha com agudeza excepcional e a perseverança traz vislumbres da vitória vindoura. Abundância de ideias e ritmo acelerado.",
        "orientacao": "Ajuste os detalhes finos do seu tesouro e tarefas. Conclua pendências intermediárias e prepare-se para colher os frutos do seu esforço."
    },
    "Lua Cheia": {
        "influencia": "O zênite do poder arcano ilumina cada torre do castelo. O magnetismo pessoal, a intuição e a capacidade de realização alcançam a potência máxima. As arcas e o espírito transbordam entusiasmo.",
        "orientacao": "Celebre as conquistas obtidas, tome decisões ousadas que demandavam bravura e irradie confiança perante seus deveres e aliados."
    },
    "Gibosa Minguante": {
        "influencia": "A colheita astral foi farta; as correntes cósmicas agora favorecem o discernimento, o compartilhamento de sabedoria e a gratidão pela prosperidade alcançada no reino.",
        "orientacao": "Avalie o que funcionou nas últimas batalhas, transmita ensinamentos e reorganize o livro de despesas do Cofre com calma e serenidade."
    },
    "Quarto Minguante": {
        "influencia": "Fase de transmutação e desapego soberano. A névoa dissipa o desnecessário para que a Rainha libere fardos e purifique o território espiritual de energias desgastantes.",
        "orientacao": "Descarte compromissos desnecessários, corte gastos supérfluos da Coroa e limpe hábitos que drenam sua mana vital."
    },
    "Minguante": {
        "influencia": "Último suspiro do luar antes do renascimento celestial. A noite convida à introspecção profunda, repouso sagrado das guerreiras e restauração plena da vitalidade e da paz mental.",
        "orientacao": "Priorize o descanso e o sono reparador. Beba infusões aromáticas, recolha-se sem culpa e permita que suas energias se renovem por completo."
    }
}

def obter_influencia_lunar(nome_fase: str = None) -> dict:
    """Retorna leitura mística completa dividida em Fase, Influência do Dia e Orientação Arcana."""
    if not nome_fase:
        nome_fase, emoji = calcular_fase_lua()
    else:
        _, emoji = calcular_fase_lua()
        for _, n, e in [
            (1.84, "Lua Nova", "🌑"), (5.53, "Crescente", "🌒"), (9.22, "Quarto Crescente", "🌓"),
            (12.91, "Gibosa Crescente", "🌔"), (16.61, "Lua Cheia", "🌕"), (20.30, "Gibosa Minguante", "🌖"),
            (23.99, "Quarto Minguante", "🌗"), (27.69, "Minguante", "🌘")
        ]:
            if n.lower() in nome_fase.lower():
                emoji = e
                nome_fase = n
                break

    info = DADOS_INFLUENCIA_LUNAR.get(nome_fase, DADOS_INFLUENCIA_LUNAR["Lua Cheia"])
    return {
        "nome": nome_fase,
        "emoji": emoji,
        "influencia": info["influencia"],
        "orientacao": info["orientacao"]
    }
