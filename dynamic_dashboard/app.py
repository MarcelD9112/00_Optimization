import streamlit as st
from pyomo.environ import ConcreteModel, Var, Objective, Constraint, SolverFactory, NonNegativeReals, maximize

# Streamlit App Title
st.title("Linear Programming Optimization Dashboard with Pyomo")
st.write("This app demonstrates solving a linear programming model using Pyomo and an open-source solver.")

# Sidebar Inputs for Constraints
st.sidebar.header("Define Your Model")
a1 = st.sidebar.number_input("Constraint 1 Coefficient for x1 (e.g., 2)", value=2)
a2 = st.sidebar.number_input("Constraint 1 Coefficient for x2 (e.g., 1)", value=1)
b1 = st.sidebar.number_input("Constraint 1 RHS (e.g., 20)", value=20)

c1 = st.sidebar.number_input("Constraint 2 Coefficient for x1 (e.g., 4)", value=4)
c2 = st.sidebar.number_input("Constraint 2 Coefficient for x2 (e.g., 3)", value=3)
b2 = st.sidebar.number_input("Constraint 2 RHS (e.g., 36)", value=36)

# Button to Solve the Model
if st.button("Solve Optimization Problem"):
    # Create the Pyomo model
    model = ConcreteModel()

    # Decision variables
    model.x1 = Var(domain=NonNegativeReals)
    model.x2 = Var(domain=NonNegativeReals)

    # Objective function
    model.obj = Objective(expr=40 * model.x1 + 30 * model.x2, sense=maximize)

    # Constraints
    model.con1 = Constraint(expr=a1 * model.x1 + a2 * model.x2 <= b1)
    model.con2 = Constraint(expr=c1 * model.x1 + c2 * model.x2 <= b2)

    # Solve the model
    solver = SolverFactory('cbc')  # Use GLPK solver (you can install it using your package manager, e.g., `brew install glpk`)
    result = solver.solve(model, tee=False)

    # Display results
    if result.solver.status == 'ok' and result.solver.termination_condition == 'optimal':
        st.success("Optimization successful!")
        st.write(f"### Results:")
        st.write(f"**Optimal value of Objective Function (Z): {model.obj():.2f}**")
        st.write(f"**Value of x1: {model.x1():.2f}**")
        st.write(f"**Value of x2: {model.x2():.2f}**")
    else:
        st.error("No optimal solution found!")
        st.write(f"Solver Status: {result.solver.status}")
        st.write(f"Termination Condition: {result.solver.termination_condition}")

# Instructions
st.write("Modify the coefficients and constraints in the sidebar, then click 'Solve Optimization Problem' to find the solution.")
