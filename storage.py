"""
Grimório V2.0 - Persistência Segura Síncrona
Gerenciamento de dados locais em JSON e Lógica de Fechamento Mensal
"""

import os
import json
import uuid
from datetime import datetime, date, timedelta

DATA_FILE_NAME = "grimorio_mobile_dados.json"

def get_data_filepath() -> str:
    """Retorna o caminho absoluto do arquivo de dados no diretório atual."""
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), DATA_FILE_NAME)

def get_default_data() -> dict:
    """Estrutura padrão inicial do Grimório."""
    hoje_str = date.today().isoformat()
    mes_atual = datetime.now().strftime("%Y-%m")
    
    return {
        "versao": "2.0.0",
        "ultimo_mes_processado": mes_atual,
        "configuracoes": {
            "nome_rainha": "Minha Rainha",
            "tema_atual": "Dark Fantasy Dourado",
            "nomes_abas": {
                "trono": "Trono",
                "quests": "Quests",
                "cofre": "Cofre",
                "forja": "Forja",
                "foco": "Foco"
            }
        },
        "reino": {
            "nome_rainha": "Minha Rainha",
            "nome_reino": "Reino de Eldoria",
            "nivel": 1,
            "titulo_nivel": "Vilarejo Inicial",
            "exp_atual": 120,
            "exp_proximo": 300,
            "ouro_tesouro": 350.0
        },
        "pet": {
            "nome": "Sir Fagulha",
            "titulo": "Gato Alado Guardião",
            "humor": "Leal e Atento",
            "nivel_afeto": 80,
            "energia": 75,
            "fome": 85,
            "ultimo_cuidado": hoje_str
        },
        "emocional": {
            "historico": [
                {
                    "data": hoje_str,
                    "humor": "Tranquila",
                    "desabafo": "Hoje iniciei a nova jornada no reino com o coração sereno.",
                    "resposta_rei": "Que a paz do teu coração seja a muralha que protege nossos dias mais felizes, minha Rainha."
                }
            ],
            "ultima_runa": {
                "nome": "Runa da Proteção",
                "simbolo": "ᛉ",
                "mensagem": "Nenhum mal ultrapassa os escudos de quem caminha com a verdade.",
                "data": hoje_str
            }
        },
        "quests": [
            {
                "id": str(uuid.uuid4()),
                "titulo": "Consagrar o Alvorecer do Reino",
                "categoria": "Principal",
                "dificuldade": "Média",
                "recompensa_ouro": 30.0,
                "recompensa_exp": 40,
                "data_limite": hoje_str,
                "concluida": True,
                "data_conclusao": hoje_str
            },
            {
                "id": str(uuid.uuid4()),
                "titulo": "Organizar os pergaminhos da semana",
                "categoria": "Diária",
                "dificuldade": "Fácil",
                "recompensa_ouro": 15.0,
                "recompensa_exp": 20,
                "data_limite": hoje_str,
                "concluida": False,
                "data_conclusao": None
            },
            {
                "id": str(uuid.uuid4()),
                "titulo": "Revisar as finanças do trono real",
                "categoria": "Coroa",
                "dificuldade": "Lendária",
                "recompensa_ouro": 60.0,
                "recompensa_exp": 80,
                "data_limite": hoje_str,
                "concluida": False,
                "data_conclusao": None
            }
        ],
        "cofre": {
            "reserva_do_reino": 1200.0,
            "divida_da_coroa": 0.0,
            "transacoes": [
                {
                    "id": str(uuid.uuid4()),
                    "tipo": "entrada",
                    "titulo": "Tributos do Comércio Nobre",
                    "valor": 1500.0,
                    "categoria": "Tributos",
                    "data": hoje_str,
                    "mes_ano": mes_atual
                },
                {
                    "id": str(uuid.uuid4()),
                    "tipo": "saida",
                    "titulo": "Provisões e Banquete da Corte",
                    "valor": 420.0,
                    "categoria": "Essenciais",
                    "data": hoje_str,
                    "mes_ano": mes_atual
                },
                {
                    "id": str(uuid.uuid4()),
                    "tipo": "saida",
                    "titulo": "Manutenção das Armaduras",
                    "valor": 180.0,
                    "categoria": "Reino",
                    "data": hoje_str,
                    "mes_ano": mes_atual
                }
            ],
            "historico_fechamentos": {
                # Exemplos de meses anteriores
            }
        },
        "forja": {
            "habitos": [
                {
                    "id": str(uuid.uuid4()),
                    "nome": "Beber Elixir Vital (2L de Água)",
                    "tipo": "HP",
                    "streak_atual": 4,
                    "melhor_streak": 12,
                    "concluido_hoje": False,
                    "datas_concluidas": []
                },
                {
                    "id": str(uuid.uuid4()),
                    "nome": "Leitura Arcana (20 minutos)",
                    "tipo": "Mana",
                    "streak_atual": 7,
                    "melhor_streak": 15,
                    "concluido_hoje": True,
                    "datas_concluidas": [hoje_str]
                },
                {
                    "id": str(uuid.uuid4()),
                    "nome": "Caminhada pelos Jardins Reais",
                    "tipo": "HP",
                    "streak_atual": 2,
                    "melhor_streak": 5,
                    "concluido_hoje": False,
                    "datas_concluidas": []
                },
                {
                    "id": str(uuid.uuid4()),
                    "nome": "Meditação & Gratidão",
                    "tipo": "Ouro",
                    "streak_atual": 5,
                    "melhor_streak": 20,
                    "concluido_hoje": True,
                    "datas_concluidas": [hoje_str]
                }
            ]
        },
        "foco": {
            "minutos_foco": 25,
            "minutos_descanso": 5,
            "total_pomodoros": 8,
            "tempo_total_minutos": 200
        }
    }

class GrimorioStorage:
    def __init__(self):
        self.filepath = get_data_filepath()
        self.data = self.carregar()
        self.verificar_fechamento_mensal()

    def carregar(self) -> dict:
        """Carrega os dados sincronamente do arquivo JSON."""
        if not os.path.exists(self.filepath):
            dados = get_default_data()
            self.salvar_dados(dados)
            return dados
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                dados = json.load(f)
            # Mescla campos faltantes se houver atualizações estruturais
            padrao = get_default_data()
            for chave, valor in padrao.items():
                if chave not in dados:
                    dados[chave] = valor
                elif isinstance(valor, dict) and isinstance(dados.get(chave), dict):
                    for subchave, subvalor in valor.items():
                        if subchave not in dados[chave]:
                            dados[chave][subchave] = subvalor
            return dados
        except Exception as e:
            print(f"[Storage] Erro ao carregar {self.filepath}: {e}. Criando novo.")
            dados = get_default_data()
            self.salvar_dados(dados)
            return dados

    def salvar(self):
        """Salva o estado atual no arquivo JSON."""
        self.salvar_dados(self.data)

    def obter_configuracoes(self) -> dict:
        """Retorna as configurações do aplicativo de forma segura."""
        if "configuracoes" not in self.data:
            self.data["configuracoes"] = {
                "nome_rainha": self.data.get("reino", {}).get("nome_rainha", "Minha Rainha"),
                "tema_atual": "Dark Fantasy Dourado",
                "nomes_abas": {
                    "trono": "Trono",
                    "quests": "Quests",
                    "cofre": "Cofre",
                    "forja": "Forja",
                    "foco": "Foco"
                }
            }
            self.salvar()
        return self.data["configuracoes"]

    def salvar_configuracoes(self, nome_rainha: str = None, tema_atual: str = None, nomes_abas: dict = None):
        """Salva alterações de perfil, tema e nomes das abas."""
        cfg = self.obter_configuracoes()
        if nome_rainha:
            cfg["nome_rainha"] = nome_rainha.strip()
            self.data["reino"]["nome_rainha"] = nome_rainha.strip()
        if tema_atual:
            cfg["tema_atual"] = tema_atual
        if nomes_abas:
            cfg["nomes_abas"].update(nomes_abas)
        self.salvar()

    def salvar_dados(self, dados: dict):
        try:
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump(dados, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"[Storage] Erro ao salvar dados: {e}")

    # ==================== FECHAMENTO MENSAL ====================
    def verificar_fechamento_mensal(self):
        """
        Lógica de Fechamento Mensal (Virada do Mês):
        - Detecta se entramos em um novo mês.
        - Consolida o mês anterior:
          * Sobras (Superávit) viram 'Ouro Guardado na Reserva do Reino'.
          * Estouros (Déficit) viram 'Dívida da Coroa'.
          * Registra no histórico de fechamentos.
          * Atualiza ultimo_mes_processado para o mês atual.
        """
        hoje = datetime.now()
        mes_atual = hoje.strftime("%Y-%m")
        ultimo_mes = self.data.get("ultimo_mes_processado", mes_atual)
        
        if ultimo_mes != mes_atual:
            # Houve virada de mês!
            transacoes_antigas = [
                t for t in self.data["cofre"]["transacoes"]
                if t.get("mes_ano") == ultimo_mes
            ]
            
            entradas_antigas = sum(t["valor"] for t in transacoes_antigas if t["tipo"] == "entrada")
            saidas_antigas = sum(t["valor"] for t in transacoes_antigas if t["tipo"] == "saida")
            saldo_antigo = entradas_antigas - saidas_antigas
            
            if saldo_antigo > 0:
                status = "superavit"
                self.data["cofre"]["reserva_do_reino"] += saldo_antigo
                reserva_add = saldo_antigo
            elif saldo_antigo < 0:
                status = "deficit"
                divida = abs(saldo_antigo)
                self.data["cofre"]["divida_da_coroa"] += divida
                reserva_add = 0.0
            else:
                status = "neutro"
                reserva_add = 0.0
                
            # Salvar no histórico de fechamentos
            if "historico_fechamentos" not in self.data["cofre"]:
                self.data["cofre"]["historico_fechamentos"] = {}
                
            self.data["cofre"]["historico_fechamentos"][ultimo_mes] = {
                "mes": ultimo_mes,
                "data_fechamento": hoje.strftime("%Y-%m-%d %H:%M"),
                "total_entradas": entradas_antigas,
                "total_saidas": saidas_antigas,
                "saldo_final": saldo_antigo,
                "status": status,
                "reserva_transferida": reserva_add
            }
            
            self.data["ultimo_mes_processado"] = mes_atual
            self.salvar()

    # ==================== SISTEMA DE EXP & REINO ====================
    TITULOS_NIVEL = [
        "Vilarejo Inicial",
        "Forte de Pedra",
        "Ducado Iluminado",
        "Baluarte dos Arcanos",
        "Reino Próspero",
        "Império Dourado",
        "Cidadela Celeste",
        "Reino Eterno"
    ]

    def adicionar_exp(self, quantidade: int) -> bool:
        """Adiciona EXP e verifica se subiu de nível. Retorna True se upou."""
        reino = self.data["reino"]
        reino["exp_atual"] += quantidade
        subiu = False
        
        while reino["exp_atual"] >= reino["exp_proximo"]:
            reino["exp_atual"] -= reino["exp_proximo"]
            reino["nivel"] += 1
            reino["exp_proximo"] = int(reino["exp_proximo"] * 1.45)
            # Atualiza título do nível
            idx = min(reino["nivel"] - 1, len(self.TITULOS_NIVEL) - 1)
            reino["titulo_nivel"] = self.TITULOS_NIVEL[idx]
            subiu = True
            
        self.salvar()
        return subiu

    def adicionar_ouro(self, valor: float):
        """Adiciona ouro no Tesouro do Reino."""
        self.data["reino"]["ouro_tesouro"] = round(self.data["reino"]["ouro_tesouro"] + valor, 2)
        self.salvar()

    def remover_ouro(self, valor: float) -> bool:
        """Remove ouro do tesouro caso haja saldo suficiente."""
        if self.data["reino"]["ouro_tesouro"] >= valor:
            self.data["reino"]["ouro_tesouro"] = round(self.data["reino"]["ouro_tesouro"] - valor, 2)
            self.salvar()
            return True
        return False

    # ==================== PET ALQUÍMICO ====================
    def alimentar_pet(self) -> str:
        pet = self.data["pet"]
        pet["fome"] = min(100, pet["fome"] + 25)
        pet["energia"] = min(100, pet["energia"] + 10)
        pet["humor"] = "Radiante e Satisfeito"
        self.adicionar_exp(5)
        self.salvar()
        return f"{pet['nome']} devorou o manjar arcano e ronrona vigorosamente! (+25 Fome, +5 EXP)"

    def brincar_pet(self) -> str:
        pet = self.data["pet"]
        if pet["energia"] < 15:
            return f"{pet['nome']} está cansado demais agora. Dê um descanso ou alimento ao guardião!"
        pet["energia"] = max(0, pet["energia"] - 15)
        pet["nivel_afeto"] = min(100, pet["nivel_afeto"] + 20)
        pet["humor"] = "Valente e Brincalhão"
        self.adicionar_exp(8)
        self.salvar()
        return f"{pet['nome']} voou em círculos brandindo sua espada de brinquedo! (+20 Afeto, +8 EXP)"

    def acariciar_pet(self) -> str:
        pet = self.data["pet"]
        pet["nivel_afeto"] = min(100, pet["nivel_afeto"] + 15)
        pet["humor"] = "Acolhido e Sereno"
        self.adicionar_exp(5)
        self.salvar()
        return f"{pet['nome']} aninhou a cabeça sob suas mãos com olhos brilhantes! (+15 Afeto, +5 EXP)"

    # ==================== QUESTS ====================
    def obter_quests_por_data(self, data_str: str) -> list:
        """Retorna todas as quests agendadas para a data específica."""
        return [q for q in self.data["quests"] if q.get("data_limite") == data_str]

    def adicionar_quest(self, titulo: str, categoria: str, dificuldade: str, data_limite: str, horario: str = None):
        recompensas_exp = {
            "Fácil": 20,
            "Média": 40,
            "Lendária": 80
        }
        exp = recompensas_exp.get(dificuldade, 25)
        nova = {
            "id": str(uuid.uuid4()),
            "titulo": titulo.strip(),
            "categoria": categoria,
            "dificuldade": dificuldade,
            "recompensa_exp": exp,
            "data_limite": data_limite,
            "horario": horario.strip() if (horario and horario.strip()) else None,
            "concluida": False,
            "data_conclusao": None
        }
        self.data["quests"].append(nova)
        self.salvar()
        return nova

    def toggle_quest_concluida(self, quest_id: str) -> dict:
        """Conclui ou desmarca uma quest, alterando EXCLUSIVAMENTE pontos de EXP de evolução do reino."""
        for q in self.data["quests"]:
            if q["id"] == quest_id:
                q["concluida"] = not q["concluida"]
                exp = q.get("recompensa_exp", 25)
                if q["concluida"]:
                    q["data_conclusao"] = date.today().isoformat()
                    self.adicionar_exp(exp)
                else:
                    q["data_conclusao"] = None
                    self.data["reino"]["exp_atual"] = max(0, self.data["reino"]["exp_atual"] - exp)
                self.salvar()
                return q
        return None

    def remover_quest(self, quest_id: str):
        self.data["quests"] = [q for q in self.data["quests"] if q["id"] != quest_id]
        self.salvar()

    # ==================== COFRE & FINANÇAS ====================
    def obter_transacoes_mes(self, mes_ano: str = None) -> list:
        if not mes_ano:
            mes_ano = datetime.now().strftime("%Y-%m")
        return [t for t in self.data["cofre"]["transacoes"] if t.get("mes_ano") == mes_ano]

    def adicionar_transacao(self, tipo: str, titulo: str, valor: float, categoria: str, data_str: str):
        dt = datetime.strptime(data_str, "%Y-%m-%d")
        mes_ano = dt.strftime("%Y-%m")
        nova = {
            "id": str(uuid.uuid4()),
            "tipo": tipo,
            "titulo": titulo.strip(),
            "valor": round(abs(valor), 2),
            "categoria": categoria,
            "data": data_str,
            "mes_ano": mes_ano
        }
        self.data["cofre"]["transacoes"].append(nova)
        self.salvar()
        return nova

    def remover_transacao(self, transacao_id: str):
        self.data["cofre"]["transacoes"] = [t for t in self.data["cofre"]["transacoes"] if t["id"] != transacao_id]
        self.salvar()

    def atualizar_teto_gastos(self, novo_teto: float):
        """Atualiza o teto orçamentário de gastos do mês."""
        self.data["cofre"]["teto_gastos_mes"] = round(max(0.0, float(novo_teto)), 2)
        self.salvar()

    def atualizar_reserva_guardada(self, nova_reserva: float):
        """Atualiza diretamente o valor guardado na Reserva do Reino."""
        self.data["cofre"]["reserva_do_reino"] = round(max(0.0, float(nova_reserva)), 2)
        self.salvar()

    def calcular_resumo_mes(self, mes_ano: str = None) -> dict:
        if not mes_ano:
            mes_ano = datetime.now().strftime("%Y-%m")
        txs = self.obter_transacoes_mes(mes_ano)
        entradas = sum(t["valor"] for t in txs if t["tipo"] == "entrada")
        saidas = sum(t["valor"] for t in txs if t["tipo"] == "saida")
        saldo = entradas - saidas
        reserva = round(self.data["cofre"].get("reserva_do_reino", 0.0), 2)
        teto = round(self.data["cofre"].get("teto_gastos_mes", 3000.0), 2)
        return {
            "mes_ano": mes_ano,
            "entradas": round(entradas, 2),
            "saidas": round(saidas, 2),
            "saldo": round(saldo, 2),
            "reserva": reserva,
            "teto_gastos": teto,
            "divida": round(self.data["cofre"].get("divida_da_coroa", 0.0), 2),
            "ouro_tesouro": round(self.data["reino"].get("ouro_tesouro", 0.0), 2)
        }

    def calcular_gastos_por_categoria(self, mes_ano: str = None) -> dict:
        """Calcula o total e a distribuição percentual de gastos por categoria no mês."""
        if not mes_ano:
            mes_ano = datetime.now().strftime("%Y-%m")
            
        txs = [t for t in self.obter_transacoes_mes(mes_ano) if t["tipo"] == "saida"]
        total_saidas = sum(t["valor"] for t in txs)
        
        agrupado = {}
        for t in txs:
            cat = t.get("categoria", "Outros")
            agrupado[cat] = agrupado.get(cat, 0.0) + t["valor"]
            
        categorias_ordenadas = []
        for cat, val in sorted(agrupado.items(), key=lambda x: x[1], reverse=True):
            pct = (val / total_saidas * 100) if total_saidas > 0 else 0.0
            categorias_ordenadas.append({
                "categoria": cat,
                "valor": round(val, 2),
                "porcentagem": round(pct, 1)
            })
            
        return {
            "total_saidas": round(total_saidas, 2),
            "categorias": categorias_ordenadas
        }

    def calcular_saude_financeira(self, mes_ano: str = None) -> dict:
        """
        Calcula o indicador de Saúde Financeira do Reino:
        - Sustentável (Verde): Superávit expressivo ou comprometimento <= 75%
        - Alerta da Coroa (Dourado/Laranja): Comprometimento entre 75% e 100%
        - Crítico / Déficit (Vermelho): Saídas > Entradas (Orçamento estourado)
        """
        resumo = self.calcular_resumo_mes(mes_ano)
        entradas = resumo["entradas"]
        saidas = resumo["saidas"]
        
        if saidas == 0:
            status = "Sustentável"
            cor = "#10B981"
            descricao = "O tesouro está intacto e protegido. Nenhuma despesa comprometeu as arcas reais este mês."
        elif entradas == 0 and saidas > 0:
            status = "Crítico / Déficit"
            cor = "#EF4444"
            descricao = "Alerta máximo: há despesas registradas sem nenhuma entrada de tributos neste ciclo!"
        else:
            taxa = saidas / entradas
            if taxa <= 0.75:
                status = "Sustentável"
                cor = "#10B981"
                descricao = f"Finanças exemplares! O reino preserva {((1 - taxa) * 100):.0f}% das riquezas arrecadadas."
            elif taxa <= 1.0:
                status = "Alerta da Coroa"
                cor = "#F59E0B"
                descricao = f"Atenção necessária: {taxa * 100:.0f}% dos tributos estão comprometidos com custos da corte."
            else:
                status = "Crítico / Déficit"
                cor = "#EF4444"
                descricao = f"Déficit ativo: os gastos excedem as receitas em {(saidas - entradas):.2f} Ouros!"
                
        return {
            "status": status,
            "cor": cor,
            "descricao": descricao,
            "saldo_atual": resumo["saldo"]
        }

    def calcular_projecao(self) -> dict:
        """
        Engine de Projeção Inteligente de 30, 60 e 90 dias:
        - Baseado na média diária de entradas vs saídas dos últimos 60 dias.
        - Acrescenta recompensas de Quests futuras já agendadas e pendentes.
        - Produz orientação temática personalizada do Rei Joaquim.
        """
        txs = self.data["cofre"]["transacoes"]
        hoje = date.today()
        limite_passado = hoje - timedelta(days=60)
        recentes = []
        for t in txs:
            try:
                t_date = datetime.strptime(t["data"], "%Y-%m-%d").date()
                if t_date >= limite_passado:
                    recentes.append(t)
            except Exception:
                continue
                
        entradas_rec = sum(t["valor"] for t in recentes if t["tipo"] == "entrada")
        saidas_rec = sum(t["valor"] for t in recentes if t["tipo"] == "saida")
        dias_base = max(1, (hoje - limite_passado).days)
        
        media_diaria_entradas = entradas_rec / dias_base
        media_diaria_saidas = saidas_rec / dias_base
        saldo_diario = media_diaria_entradas - media_diaria_saidas
        
        saldo_atual_mes = self.calcular_resumo_mes()["saldo"]
        reserva_reino = self.data["cofre"].get("reserva_do_reino", 0.0)
        base_acumulada = saldo_atual_mes + reserva_reino
        
        saldo_30d = base_acumulada + (saldo_diario * 30)
        saldo_60d = base_acumulada + (saldo_diario * 60)
        saldo_90d = base_acumulada + (saldo_diario * 90)
        
        if saldo_90d >= base_acumulada * 1.25 and saldo_diario > 0:
            status = "prospero"
            msg_rei = (
                f"Minha Rainha, as estrelas favorecem nosso reinado! Se o ritmo de tributos se mantiver firme, "
                f"nossa reserva alcançará {saldo_90d:,.0f} Ouros em 90 dias. Teu governo é sinônimo de prosperidade."
            )
        elif saldo_90d >= 0 and saldo_diario >= 0:
            status = "sustentavel"
            msg_rei = (
                f"Se o ritmo de gastos se mantiver equilibrado, a reserva alcançará {saldo_60d:,.0f} Ouros em 60 dias "
                f"e {saldo_90d:,.0f} Ouros em 90 dias. Tua prudência resguarda o castelo com serenidade."
            )
        elif saldo_90d >= 0 and saldo_diario < 0:
            status = "alerta"
            msg_rei = (
                f"Atenção da Coroa, Rainha: embora ainda haja reserva, o ritmo diário consome mais do que arrecadamos. "
                f"Em 90 dias nosso tesouro diminuirá para {saldo_90d:,.0f} Ouros. Recomendo conter despesas secundárias."
            )
        else:
            status = "risco_deficit"
            deficit_previsto = abs(saldo_90d)
            msg_rei = (
                f"Alerta Real Urgente: Se mantivermos este padrão de despesas, o reino enfrentará um déficit projetado "
                f"de {deficit_previsto:,.0f} Ouros em 90 dias. É tempo de convocar austeridade orçamentária."
            )
            
        return {
            "media_diaria_entradas": round(media_diaria_entradas, 2),
            "media_diaria_saidas": round(media_diaria_saidas, 2),
            "saldo_diario": round(saldo_diario, 2),
            "projecao_30d": round(saldo_30d, 2),
            "projecao_60d": round(saldo_60d, 2),
            "projecao_90d": round(saldo_90d, 2),
            "status": status,
            "mensagem_rei": msg_rei
        }

    # ==================== FORJA & HÁBITOS ====================
    def alternar_habito_hoje(self, habito_id: str) -> dict:
        hoje_str = date.today().isoformat()
        for h in self.data["forja"]["habitos"]:
            if h["id"] == habito_id:
                datas = set(h.get("datas_concluidas", []))
                if hoje_str in datas:
                    datas.remove(hoje_str)
                    h["concluido_hoje"] = False
                    h["streak_atual"] = max(0, h.get("streak_atual", 1) - 1)
                else:
                    datas.add(hoje_str)
                    h["concluido_hoje"] = True
                    h["streak_atual"] = h.get("streak_atual", 0) + 1
                    if h["streak_atual"] > h.get("melhor_streak", 0):
                        h["melhor_streak"] = h["streak_atual"]
                    self.adicionar_exp(12)
                    self.adicionar_ouro(5.0)
                    
                h["datas_concluidas"] = sorted(list(datas))
                self.salvar()
                return h
        return None

    def adicionar_habito(self, nome: str, tipo: str):
        novo = {
            "id": str(uuid.uuid4()),
            "nome": nome.strip(),
            "tipo": tipo,
            "streak_atual": 0,
            "melhor_streak": 0,
            "concluido_hoje": False,
            "datas_concluidas": []
        }
        self.data["forja"]["habitos"].append(novo)
        self.salvar()
        return novo

    def remover_habito(self, habito_id: str):
        self.data["forja"]["habitos"] = [h for h in self.data["forja"]["habitos"] if h["id"] != habito_id]
        self.salvar()

    # ==================== TRONO & EMOCIONAL ====================
    def registrar_emocional(self, humor: str, desabafo: str, resposta_rei: str):
        hoje_str = date.today().isoformat()
        reg = {
            "data": hoje_str,
            "humor": humor,
            "desabafo": desabafo.strip(),
            "resposta_rei": resposta_rei
        }
        self.data["emocional"]["historico"].insert(0, reg)
        self.adicionar_exp(15)
        self.salvar()
        return reg

    def salvar_runa(self, runa: dict):
        runa["data"] = date.today().isoformat()
        self.data["emocional"]["ultima_runa"] = runa
        self.salvar()


# Instância Global de Armazenamento
storage = GrimorioStorage()
