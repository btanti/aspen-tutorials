# Initial Flowsheet
- Flowsheet options: General with Metric  units template
- Property method: UNIFAC
- Feed stream #1: 200 kg/min ethanol, 25 C
- Feed stream #2: 261 kg/min acetic acid, 25 C

# Reactor
- REquil
  - Temperature: 55 C
  - Pressure: 1 bar
  - Reactions: ETHANOL + ACETIC ACID -> ETHYL ACETATE + WATER
    - Coefficients: -1, 1 (reactants), 1, 0 (products)

# Reactor (RadFrac)
- RadFrac specifications
  - Stages: 23
  - Type: Total condenser
  - Reflux Ratio: 3 (mol ratio)
  - Reboiler duty: 3500 kJ/sec
  - Feed stage: 12, on-stage

# Heat Exchanger
  - 2 HeatX blocks, one per feed stream
  - Hot water stream: 
    - Temperature: 80 C
    - Pressure: 1 bar
    - Flowrate: 200 kg/min.
  - HeatX:
    - Model fidelity: Shortcut
    - Outlet temperature:  55C
    - Min temperature approach: 5 C

# Pump
  - 2 Pumps, each before their respective heat exchanger
  - Discharge pressure: 1 bar

# Design Specifications
  - Starts from Ch 2.3
  - RadFrac block:
    - Stages: 10
    - Type: Total condenser
    - Reflux ratio: 2 (mol ratio)
    - Bottoms rate: 20 kg/min
    - Feed: Stage 6 (On-stage)
    - Condenser pressure: 1 bar
    - Column design spec:
      - Specification RECOVERY
        - Type: Mol recovery, .999
        - Component: acetic-acid
        - Product stream: column bottoms
      - Vary bottoms rate
        - Lowerbound: 2000 kg/hr
        - Upperbound: 5000 kg/hr
    - Convergence options
      - Iterations: 200
  - Mixer:
  - Decanter:
    - Pressure: 1 bar
    - Temperature: 25  C
    - 2nd liquid phase: water
  - RadFrac #2:
    - Stages: 15
    - Type: total condenser
    - Distillate rate: 18500 kg/hr
    - Reflux ratio: 5 (mol  ratio)
    - Feed: Stage 8
    - Condenser pressure: 1 bar
  - Additional streams:
    - Water, 25 C, 1 bar, 200kg/min into the mixer.
  - Design Specification 2:
    - AAPURITY (under flowsheeting options)
    - Variable -> PURITY
    - Type: Mass-Frac
    - Final ethyl acetate stream, componentis ethyl acetate
    - Specifications:
      - PURITY, target .98, tolerance .0001
    - Vary:
      - Mass-Flow, WATER stream, WATER component, kg/min units
      - Lower bound: 200
      - Upper bound: 800

# Sensitivity Analysis
  - New variable -> Block-Var -> RadFrac #2
  - MOLE-RR:
    - Range is 2.5 to 6, 150 points of evaluation
    - Define tab -> New Variable:
      - Type: Mass-Flow
      - Stream: Distillate  out top of column
      - Component: Ethanol
      - Units: kg/hr
    - Tabulate  tab -> Fill Variables


Note: any parameters not specified in this memo assume their default values.