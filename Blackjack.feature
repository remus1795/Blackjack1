Feature: BlackJack


Scenario: Inicio

    Given Quiere 'S'jugar
    When Crea naipes
    Then Reparte jugador


Scenario: Tiene aces

    Given Mano jugador
    When Mano jugador no vacia
    Then Pregunta valor

Scenario: Otra carta

    Given Mano jugador
    When Mano jugador no vacia
    And confirma carta extra 'S'
    Then Reparte carta extra

Scenario: Contar

    Given Mano jugador
    When Mano jugador no vacia
    Then Contar mano

Scenario: Planta
    Given Confirma carta extra 'N'
    When Mano jugador no vacia
    Then Juega IA
    And planta jugador

Scenario Ganador
    Given Mano jugador
    And Juego IA
    When Planta jugador
    And Planta_Ia
    Then Decide ganador

    
      
