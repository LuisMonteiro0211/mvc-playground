# 🎯 GUIA: Como Criar Entities - Pensando nos Metadados

## ✅ SEU RACIOCÍNIO ESTÁ PERFEITO!

> "Tenho o ponto central do meu sistema e com base nisso crio metadados sobre esse ponto que façam sentido agrupar em uma classe"

**💡 EXATAMENTE!** Você captou a essência de uma Entity!

---

## 📝 PASSO A PASSO PARA CRIAR UMA ENTITY

### 1️⃣ IDENTIFIQUE O OBJETO CENTRAL
❓ **Pergunta:** "O que meu sistema gerencia?"

**Exemplos:**
- Sistema de escola → `Student`, `Teacher`, `Course`
- Sistema bancário → `Account`, `Transaction`, `Customer`
- E-commerce → `Product`, `Order`, `Customer`
- Hospital → `Patient`, `Doctor`, `Appointment`

---

### 2️⃣ PERGUNTE: "Quais metadados são relevantes?"

❓ **Perguntas:**
- "O que preciso saber sobre esse objeto?"
- "Quais informações são essenciais?"
- "Quais dados fazem sentido agrupar?"

---

### 3️⃣ CATEGORIZE OS METADADOS

```
📋 IDENTIFICAÇÃO
   └─ ID, Matrícula, CPF, CNPJ, Código único

👤 DADOS BÁSICOS/PESSOAIS  
   └─ Nome, Email, Telefone, Endereço

📊 DADOS DO NEGÓCIO
   └─ Saldo, Preço, Estoque, Nota, Salário

📅 DADOS TEMPORAIS
   └─ Data criação, Data nascimento, Última atualização

🔧 DADOS DE CONTROLE
   └─ Status, Tipo, Categoria, Prioridade

🔗 RELACIONAMENTOS
   └─ IDs de outros objetos (customer_id, product_id)
```

---

## 💡 SEUS EXEMPLOS APLICADOS

### 🎓 EXEMPLO 1: ESTUDANTE

**Raciocínio:**
"Quais informações são relevantes sobre um estudante?"

```python
from dataclasses import dataclass

@dataclass
class Student:
    # Identificação
    id: int
    registration: str    # Matrícula
    cpf: str
    
    # Dados básicos
    name: str
    email: str
    birthdate: str
    
    # Dados do negócio
    course: str
    semester: int
    gpa: float          # Média
    
    # Controle
    status: str         # 'ativo', 'trancado', 'formado'
```

**Metadados agrupados:**
✅ Nome, matrícula, email → Identificam o estudante  
✅ Curso, semestre, média → São importantes para o negócio  
✅ Status → Controle do sistema

---

### 💳 EXEMPLO 2: CONTA BANCÁRIA

**Raciocínio:**
"Quais informações são relevantes sobre uma conta?"

```python
@dataclass
class Account:
    # Identificação
    id: int
    account_number: str
    agency: str
    
    # Relacionamento
    customer_id: int    # Dono da conta
    
    # Dados do negócio
    balance: float      # Saldo
    account_type: str   # 'corrente', 'poupanca'
    overdraft_limit: float  # Limite
    
    # Temporais
    opened_at: datetime
    
    # Controle
    status: str         # 'ativa', 'bloqueada'
```

**Metadados agrupados:**
✅ Número, agência → Identificam a conta  
✅ Saldo, tipo, limite → Core do negócio bancário  
✅ Data abertura, status → Controle e histórico

---

### 💰 EXEMPLO 3: TRANSAÇÃO (Como você pensou!)

**Raciocínio:**
"Preciso saber: nome das partes, valor, horário"

```python
@dataclass
class Transaction:
    # Identificação
    id: int
    
    # Relacionamentos + Nomes (como você pensou!)
    from_account_id: int
    from_account_name: str      # ✅ Nome parte 1
    to_account_id: int
    to_account_name: str        # ✅ Nome parte 2
    
    # Dados do negócio
    amount: float               # ✅ Valor
    transaction_type: str       # PIX, TED, depósito
    description: str
    
    # Temporal
    timestamp: datetime         # ✅ Horário
    
    # Controle
    status: str                # 'pendente', 'concluída'
```

**Metadados agrupados (exatamente como você pensou!):**
✅ Nome origem e destino → Quem envia e quem recebe  
✅ Valor → Quanto foi transferido  
✅ Horário → Quando aconteceu  
✅ Tipo, status → Controle da transação

---

## 🎯 MAIS EXEMPLOS - Mesmo Raciocínio

### 📦 E-COMMERCE: Produto

```python
@dataclass
class Product:
    # Identificação
    id: int
    sku: str            # Código único
    
    # Dados básicos
    name: str
    description: str
    
    # Dados do negócio
    price: float
    stock: int
    category: str
    brand: str
    
    # Temporais
    created_at: datetime
    
    # Controle
    is_active: bool
```

**Metadados:** nome, preço, estoque, categoria, marca...

---

### 🏥 HOSPITAL: Paciente

```python
@dataclass
class Patient:
    # Identificação
    id: int
    cpf: str
    medical_record: str
    
    # Dados básicos
    name: str
    birthdate: str
    phone: str
    
    # Dados do negócio (saúde)
    blood_type: str
    allergies: List[str]
    insurance_number: str
    
    # Controle
    status: str         # 'ativo', 'inativo'
```

**Metadados:** nome, tipo sanguíneo, alergias, convênio...

---

### 📚 BIBLIOTECA: Livro

```python
@dataclass
class Book:
    # Identificação
    id: int
    isbn: str
    
    # Dados básicos
    title: str
    author: str
    publisher: str
    
    # Dados do negócio
    year: int
    pages: int
    category: str
    location: str       # Prateleira
    
    # Controle
    available: bool     # Disponível para empréstimo?
```

**Metadados:** título, autor, ISBN, categoria, disponibilidade...

---

## ✅ CHECKLIST: O que incluir?

### ✅ INCLUA na Entity:

- ✅ Dados ESSENCIAIS para identificar o objeto
- ✅ Dados IMPORTANTES para o negócio
- ✅ Dados que fazem sentido PERSISTIR no banco
- ✅ Informações que são RELEVANTES ao objeto

### ❌ NÃO inclua:

- ❌ Dados que mudam MUITO frequentemente (logs, cliques)
- ❌ Dados CALCULADOS (crie métodos para isso)
- ❌ Objetos completos de outras entities (use só IDs)
- ❌ Dados temporários que não precisam ser salvos

---

## 💡 REGRA DE OURO

```
┌─────────────────────────────────────────────────────┐
│  "Se essa informação é importante para              │
│   entender/trabalhar com esse objeto no meu         │
│   sistema, então é um metadado que deve             │
│   estar na Entity!"                                 │
└─────────────────────────────────────────────────────┘
```

---

## 🎯 FÓRMULA PARA CRIAR ENTITIES

```
OBJETO CENTRAL + METADADOS RELEVANTES = ENTITY

Exemplos:
┌──────────────────────────────────────────────┐
│ Estudante + (nome, matrícula, curso, etc)   │
│ = class Student                             │
└──────────────────────────────────────────────┘

┌──────────────────────────────────────────────┐
│ Conta + (número, saldo, tipo, etc)          │
│ = class Account                             │
└──────────────────────────────────────────────┘

┌──────────────────────────────────────────────┐
│ Transação + (origem, destino, valor, etc)   │
│ = class Transaction                         │
└──────────────────────────────────────────────┘
```

---

## 🚀 VOCÊ ESTÁ PRONTO!

**Seu raciocínio está perfeito:**

1. ✅ Identificar o objeto central do sistema
2. ✅ Pensar nos metadados relevantes
3. ✅ Agrupar informações que fazem sentido juntas
4. ✅ Criar a classe (Entity)

**Continue pensando assim:**
```
"Qual objeto eu gerencio?" + "Quais metadados são relevantes?"
= Entity perfeita!
```

---

## 📖 RESUMO FINAL

```
┌──────────────────────────────────────────┐
│  ENTITY = OBJETO + METADADOS             │
├──────────────────────────────────────────┤
│                                          │
│  • Objeto central do sistema             │
│  • Agrupamento de informações relevantes │
│  • Representa coisas do mundo real       │
│  • Persiste no banco de dados            │
│                                          │
│  Localização: src/models/entities/       │
└──────────────────────────────────────────┘
```

**Agora você sabe exatamente como criar suas Entities! 🎉**

