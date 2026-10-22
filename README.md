# Amanda da Mata

Systems Analysis and Development student in Brazil, focused on **back-end development with Java and Python**.
I am looking for a **remote software engineering internship or junior role**.

I build small applications with real business rules, automated tests, continuous integration, and documentation that explains *why* the code is written the way it is.

[LinkedIn](https://www.linkedin.com/in/amanda-da-mata-492106288/) · [Projects](#projects) · [Versão em português](#versão-em-português)

---

## Projects

### [VetCare Scheduler](https://github.com/Amandadamata/vetcare-scheduler-java) · Java 21

Command-line application for veterinary appointments: one schedule per vet or room, a calculated triage priority, an appointment life cycle, and deletion or anonymization of personal data. Data is stored locally as JSON.

- Layered design (`cli`, `service`, `repository`, `persistence`, `model`) wired by constructor injection
- Conflicts checked per schedule; back-to-back appointments allowed
- Appointment status as a state machine (scheduled → completed, no-show, or cancelled)
- Deletion and anonymization that keep every reference valid and are undone if saving fails
- Older data files migrated automatically after validation and a backup
- JUnit 6 tests, including a real file from the previous release and complete menu sessions; CI on Java 21 and 25

[Architecture](https://github.com/Amandadamata/vetcare-scheduler-java/blob/main/docs/ARCHITECTURE.md) · [Design decisions](https://github.com/Amandadamata/vetcare-scheduler-java/blob/main/docs/DESIGN_DECISIONS.md) · [Tests](https://github.com/Amandadamata/vetcare-scheduler-java/blob/main/docs/TESTING.md)

### [Banking System](https://github.com/Amandadamata/sistema-bancario-java) · Java 17

Command-line banking application with checking and savings accounts, CPF validation, and SQLite persistence.

- Exact money arithmetic with `BigDecimal`; money stored as integer cents in the database
- Each operation saved in one JDBC transaction, so a transfer is stored on both sides or neither
- Changes undone in memory if saving fails; stored statements re-checked against balances on load
- CPF check digits validated, with the full number never shown in messages
- Unit and integration tests with a real SQLite file; CI on Java 17, 21 and 25

[Architecture](https://github.com/Amandadamata/sistema-bancario-java/blob/main/docs/ARCHITECTURE.md) · [Design decisions](https://github.com/Amandadamata/sistema-bancario-java/blob/main/docs/DESIGN_DECISIONS.md) · [Tests](https://github.com/Amandadamata/sistema-bancario-java/blob/main/docs/TESTING.md)

## Skills

| Used in these projects | Currently studying |
|---|---|
| Java (17, 21), object-oriented programming, collections, `java.time` | Python |
| SQL with SQLite and JDBC, transactions | REST APIs |
| JUnit 6, Maven, Gson, Git, pull requests, GitHub Actions | |

## How I work

- I work with pull requests that describe the problem, the fix, and how it was tested.
- Tests check behavior, including what must **not** change when an operation fails.
- Known limitations are written down in each README instead of being hidden.

## Background

Before moving into technology, I worked as an English teacher. That experience shaped how I communicate and how I document my work.

---

## Versão em português

<details>
<summary>Ler em português</summary>

<br>

Sou estudante de **Análise e Desenvolvimento de Sistemas** no Brasil, com foco em **desenvolvimento back-end com Java e Python**. Busco **estágio ou vaga júnior remota** em engenharia de software.

Desenvolvo aplicações pequenas com regras de negócio reais, testes automatizados, integração contínua e documentação que explica *por que* o código foi escrito daquela forma.

**Projetos**

- [VetCare Scheduler](https://github.com/Amandadamata/vetcare-scheduler-java) (Java 21): agenda veterinária com uma agenda por veterinário ou sala, prioridade de triagem, ciclo de vida das consultas, exclusão e anonimização de dados pessoais e persistência em JSON com migração de arquivos antigos. Arquitetura em camadas, testes JUnit 6 e CI.
- [Sistema Bancário](https://github.com/Amandadamata/sistema-bancario-java) (Java 17): contas corrente e poupança com valores exatos (`BigDecimal`), validação de CPF e persistência em SQLite com uma transação JDBC por operação. Testes de unidade e de integração e CI com Java 17, 21 e 25.

Cada projeto tem README em inglês e em português.

**Uso nos projetos:** Java, orientação a objetos, SQL com SQLite e JDBC, JUnit 6, Maven, Gson, Git e GitHub Actions.
**Estudando:** Python e APIs REST.

Antes da tecnologia, trabalhei como professora de inglês.

[LinkedIn](https://www.linkedin.com/in/amanda-da-mata-492106288/)

</details>
