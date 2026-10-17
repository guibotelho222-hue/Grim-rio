# 📖 Grimório V2.0 — Dark Fantasy RPG & Crônicas do Reino

Aplicativo definitivo de produtividade, acolhimento emocional e gestão pessoal construído com uma estética **Dark Fantasy moderna, limpa e profissional**.

---

## 🏛️ 1. Estrutura do Projeto

O projeto está localizado em:
`C:\Users\guilherme\.gemini\antigravity\scratch\GrimórioV2.0`

```
GrimórioV2.0/
│
├── assets/
│   ├── logo.ico               <- Ícone oficial do Gatinho Cavaleiro para executável e janela (.exe)
│   ├── logo.png               <- Logo oficial do Gatinho Cavaleiro em alta resolução
│   ├── mascote.png            <- Ilustração transparente do Gato Guardião Alado
│   ├── rei_joaquim.png        <- Ilustração do Rei Joaquim para a Aba Trono
│   ├── rei_joaquim_trono.png  <- Sprite do Rei Joaquim no trono
│   └── rei_joaquim_sheet.png  <- Spritesheet mestre
│
├── components/
│   ├── common_ui.py           <- Header Fixo (Lua, Runa, Status, Configs), Modal de Configurações e Cards
│   └── mascote_vector.py      <- Visual 100% vetorial em código Flet do Mascote Guardião Alado
│
├── tabs/
│   ├── tab_trono.py           <- Aba 1: Trono Real (Dedicada ao Rei Joaquim, Diálogos e Audiência Real)
│   ├── tab_quests.py          <- Aba 2: Quests (Calendário Interativo, Missões e Ouro)
│   ├── tab_cofre.py           <- Aba 3: Cofre (Fechamento Mensal, Projeção e Histórico)
│   ├── tab_forja.py           <- Aba 4: Forja (Evolução do Império e Hábitos Mana/HP)
│   └── tab_foco.py            <- Aba 5: Foco (Poção Alquímica Pomodoro e Timer Síncrono)
│
├── grimorio_mobile_dados.json <- Persistência de dados local síncrona
├── theme.py                   <- Paletas Dark Fantasy Dinâmicas, Cálculo Lunar e Estilos
├── storage.py                 <- Engine de persistência, configurações e fechamento mensal
├── oracle.py                  <- Diálogos sábios do Rei Joaquim e 12 Runas Místicas
├── splash_screen.py           <- Splash screen oficial com Gatinho Cavaleiro e borda dourada
├── main.py                    <- Ponto de entrada síncrono oficial e roteador de abas
├── build_exe.bat              <- Script de compilação rápida para Windows (.exe)
├── pyproject.toml             <- Configuração para Android (com.grimorio.v2)
└── README.md                  <- Documentação técnica do projeto
```

---

## ⚡ 2. Arquitetura & Novas Funcionalidades (ETAPA 1)

- **Logo e Ícone Oficial**: A imagem oficial do Gatinho Cavaleiro foi configurada como única logo e ícone do sistema em `assets/logo.png` e `assets/logo.ico`.
- **Header Fixo Multifuncional**: Presente no topo de todas as abas contendo:
  - `[Engrenagem Configs]`: Acesso direto ao modal de configurações.
  - `[Fase da Lua]`: Cálculo astronômico em tempo real da fase lunar atual.
  - `[Runa Diária]`: Glifo e nome da runa do dia com mensagem em tooltip.
  - `[Nível e Reserva de Ouro]`: Saldo do tesouro e nível do reino.
  - Barra de EXP com o nome personalizado da Rainha.
- **Módulo de Configurações**:
  - Personalização do Nome da Rainha / Personagem.
  - Personalização dos títulos das 5 abas principais.
  - Seletor de Paletas Dark Fantasy (*Dark Fantasy Dourado*, *Roxo Arcano*, *Esmeralda Obscura*, *Chumbo Sóbrio*) com troca dinâmica de cores.
- **Aba Trono Exclusiva do Rei Joaquim**:
  - Destaque nobre para o Rei Joaquim com balão de fala afetuoso, formulário para Audiência Real / Suporte Emocional e histórico de conselhos recebidos (zero elementos de tamagotchi/pet).
- **100% Síncrono & Estável**: Zero loops assíncronos e uso exclusivo de `botao_preenchido` / `ft.FilledButton` prevenindo erros de atributos.

---

## 🌟 3. Visão das 5 Abas Principais

### 👑 Aba 1: Trono (Acolhimento & Suporte Emocional)
- **Rei Joaquim**: Ilustração em destaque (`assets/rei_joaquim.png`) com balões de conversa, diálogos carinhosos e acolhedores direcionados à Rainha.
- **Questionário Emocional Diário**: Registro rápido do coração (Radiante, Tranquila, Cansada, Ansiosa, Sobrecarregada, Vitoriosa) com campo de desabafo.
- **Resposta Empática em Tempo Real**: Joaquim analisa a mensagem e devolve um conselho afetuoso e acolhedor.
- **Oráculo Real**: Banco de 12 Runas Nórdicas/Arcanas para tiragem diária com mensagens sábias.
- **Pet Alquímico (Sir Fagulha)**: Mascote em armadura com botões operacionais (*Alimentar*, *Treinar*, *Acariciar*) e barras de vitalidade.

### 📜 Aba 2: Quests (Calendário & Missões)
- **Calendário Dinâmico**: Navegação livre entre meses passados e futuros com seleção de qualquer dia.
- **Mural de Quests**: Adição, conclusão e exclusão de tarefas categorizadas (*Principal*, *Diária*, *Coroa*, *Secundária*).
- **Evolução do Império**: Concluir tarefas concede EXCLUSIVAMENTE pontos de EXP (`recompensa_exp`) para o nível do Reino, mantendo o Cofre financeiro estritamente real e protegido de inflação fictícia.

### 🪙 Aba 3: Cofre (Finanças Inteligentes & Gestão Financeira Real)
- **Finanças 100% Reais**: O Saldo do Cofre e a Reserva Guardada alteram-se unicamente mediante lançamentos contábeis reais (entradas e saídas digitadas pela usuária).
- **Edição Direta de Teto & Reserva**: Botões rápidos de lápis (`ft.IconButton`) ao lado dos valores de **Teto de Gastos Mensal** e **Reserva Guardada**, abrindo modais de ajuste imediato salvos no JSON.
- **Barra de Progresso do Teto Orçamentário**: Monitoramento visual do limite mensal de gastos com cores dinâmicas (Verde se $\le 75\%$, Laranja se $75\%-100\%$, Vermelho se estourado).
- **Lógica de Fechamento Mensal (Virada do Mês)**:
  - Na virada de mês, o fluxo de receitas/despesas zera para iniciar o novo ciclo limpo.
  - Sobras (**Superávit**) são transferidas como reserva para a **Reserva do Reino**.
  - Estouros (**Déficit**) acionam o alerta régio de **Dívida da Coroa** com metas de ajuste.
- **Cartão de Saúde Financeira do Reino**:
  - Avaliação automática do orçamento com indicadores de status: *Sustentável* (Verde), *Alerta da Coroa* (Dourado/Laranja) e *Crítico / Déficit* (Vermelho).
- **Dashboard Gráfico de Gastos por Categoria**:
  - Barras proporcionais e percentuais por categoria (*Alimentação*, *Moradia*, *Lazer*, *Saúde*, *Investimentos*, *Essenciais*, *Tributos*, *Reino & Armas*, *Poupança*, *Outros*).
- **Engine de Projeção Inteligente (30, 60 e 90 dias)**:
  - Previsão futura do tesouro baseada estritamente no fluxo diário médio real de entradas e saídas.
  - Card de orientação temática e conselhos estratégicos do Rei Joaquim.
- **Histórico & Balanços Anteriores**: Modal com demonstrativos detalhados de todos os ciclos passados consolidados.

### 🔨 Aba 4: Forja (Hábitos & Evolução)
- **Evolução do Império**: Rastreio do nível do império (Vilarejo Inicial, Forte de Pedra, Ducado Iluminado, etc.) com barras de experiência.
- **Hábitos Mana/HP**: Barras no estilo Dark Fantasy com fogo de sequência (streak 🔥) para virtudes de vitalidade, foco mental e disciplina financeira.

### 🧪 Aba 5: Foco (Poção Alquímica Pomodoro)
- **Frasco com Líquido Dinâmico**: Poção mágica cujo nível se altera visualmente à medida que o tempo avança.
- **Modos de Foco & Descanso**: Alternância com ciclos predefinidos (15, 25, 45, 50 min).
- **Alertas**: Notificações comemorativas e ganho de EXP/Ouro a cada poção consumada.

---

## 🚀 4. Como Executar

### Pré-requisitos
Ter o Python instalado com Flet e Pillow:
```bash
pip install flet pillow
```

### Executar o Grimório em Modo de Desenvolvimento
No diretório `C:\Users\guilherme\.gemini\antigravity\scratch\GrimórioV2.0`:
```bash
python main.py
```

---

## 📦 5. Compilação Oficial para Windows (.exe)

O script `build_exe.bat` automatiza a geração do executável oficial standalone.

Execute via terminal ou duplo clique:
```cmd
build_exe.bat
```
Ou execute o comando de compilação:
```cmd
python -m PyInstaller --noconfirm --onedir --windowed --name "Grimório" --icon "assets/logo.ico" --add-data "assets;assets" --add-data "grimorio_mobile_dados.json;." main.py
```
O executável standalone com ícone oficial e assets integrados é gerado em:
`dist\Grimório\Grimório.exe`

---

## 📱 6. Compilação para Android (.apk)

Com o Flutter/Android SDK configurado, execute:
```bash
flet build apk --org com.grimorio.v2
```
O identificador de pacote limpo `com.grimorio.v2` garantirá a instalação definitiva no dispositivo.

