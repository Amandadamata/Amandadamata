# Amanda da Mata

Systems Analysis and Development student in Brazil, focused on **back-end development with Java and Python**.
I am looking for a **remote software engineering internship or junior role**.

I build small applications with real business rules, automated tests, continuous integration, and documentation that explains *why* the code is written the way it is.

[LinkedIn](https://www.linkedin.com/in/amanda-da-mata-492106288/) · [Projects](#projects) · [Versão em português](#versão-em-português)

---

## Projects

### [VetCare Scheduler](https://github.com/Amandadamata/vetcare-scheduler-java) · Java 21

Command-line application for veterinary appointments: calculates a triage priority, prevents overlapping bookings, and stores data locally as JSON.

- Layered design (`cli`, `service`, `repository`, `persistence`, `model`) wired by constructor injection
- Interval-based conflict detection that allows back-to-back appointments
- Data loaded from disk is validated before use; a damaged file is reported and never overwritten
- JUnit 6 tests for services, persistence, invalid data and complete menu sessions; GitHub Actions CI

[Architecture](https://github.com/Amandadamata/vetcare-scheduler-java/blob/main/docs/ARCHITECTURE.md) · [Design decisions](https://github.com/Amandadamata/vetcare-scheduler-java/blob/main/docs/DESIGN_DECISIONS.md) · [Tests](https://github.com/Amandadamata/vetcare-scheduler-java/blob/main/docs/TESTING.md)

### [Banking System](https://github.com/Amandadamata/sistema-bancario-java) · Java 17

Command-line banking application with checking and savings accounts.

- Exact money arithmetic with `BigDecimal` and explicit rounding (`HALF_EVEN`)
- Overdraft implemented through polymorphism; operations validate everything before changing any balance
- Monthly savings yield tested with an injected `Clock`
- JUnit 6 tests for business rules and menu flows; CI on Java 17 and 21

[Architecture](https://github.com/Amandadamata/sistema-bancario-java/blob/main/docs/ARCHITECTURE.md) · [Design decisions](https://github.com/Amandadamata/sistema-bancario-java/blob/main/docs/DESIGN_DECISIONS.md) · [Tests](https://github.com/Amandadamata/sistema-bancario-java/blob/main/docs/TESTING.md)

## Skills

| Used in these projects | Currently studying |
|---|---|
| Java (17, 21), object-oriented programming, collections, `java.time` | Python |
| JUnit 6, Maven, Gson | SQL and relational databases |
| Git, pull requests, GitHub Actions | REST APIs |

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

- [VetCare Scheduler](https://github.com/Amandadamata/vetcare-scheduler-java) (Java 21): agenda veterinária com prioridade de triagem, detecção de conflitos de horário e persistência em JSON validada ao carregar. Arquitetura em camadas, testes JUnit 6 e CI.
- [Sistema Bancário](https://github.com/Amandadamata/sistema-bancario-java) (Java 17): contas corrente e poupança com valores monetários exatos (`BigDecimal`), cheque especial por polimorfismo e rendimento mensal testado com `Clock` injetado. Testes JUnit 6 e CI com Java 17 e 21.

Cada projeto tem README em inglês e em português.

**Uso nos projetos:** Java, orientação a objetos, JUnit 6, Maven, Gson, Git e GitHub Actions.
**Estudando:** Python, SQL e APIs REST.

Antes da tecnologia, trabalhei como professora de inglês.

[LinkedIn](https://www.linkedin.com/in/amanda-da-mata-492106288/)

</details>
