# Лабораторная работа по Дискретной математике ИТМО
## Машина Тьюринга
- [условия](problems.pdf)

### Литералы
<state>: `java.lang.String`
<letter>: `java.lang.String`
<state>: `[^ | < | >]`

### Входной формат одноленточной машины
start: <start name>
accept: <accept name>
reject: <reject name>
blank: <blank name>

<state> <letter> -> <state_to> <letter_to> <direction>

Example:
> start: s
> accept: ac
> reject: rj
> blank: _
> s _ -> ac _ ^
> s 0 -> n _ >
> n 0 -> s _ >
> n _ -> rj _ >

	
### Входной формат многолетночной машины

<n = ntapes> (Количество лент)
(<state> <letter_1> <letter_2> ... <letter_n> -> <state_to> <letter_to_1> <direction_1> ... <letter_to_n> <direction_n>)
Стартовое состояние - S, допускающее - AC, отвергающее - RJ, blank - _ (подчёркивание)

Example:
> 2
> S 0 0 -> a 1 > 2 >
> a 1 1 -> S 333 ^ szdf <
> a 2 3 -> AC 333 ^ _ ^ 