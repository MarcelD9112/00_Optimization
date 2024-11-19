import streamlit as st
from pulp import LpMaximize, LpProblem, LpVariable, value

# Streamlit App Title
st.title("Linear Programming Optimization Dashboard")
st.write("This app demonstrates solving a simple linear programming model using PuLP.")

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
    # Create a linear programming model
    model = LpProblem(name="linear-program", sense=LpMaximize)

    # Decision variables
    x1 = LpVariable(name="x1", lowBound=0)
    x2 = LpVariable(name="x2", lowBound=0)

    # Objective function
    model += 40 * x1 + 30 * x2, "Objective"

    # Constraints
    model += a1 * x1 + a2 * x2 <= b1, "Constraint 1"
    model += c1 * x1 + c2 * x2 <= b2, "Constraint 2"

    # Solve the model
    status = model.solve()

    # Display results
    if status == 1:  # Optimal solution found
        st.success("Optimization successful!")
        st.write(f"### Results:")
        st.write(f"**Optimal value of Objective Function (Z): {value(model.objective)}**")
        st.write(f"**Value of x1: {x1.varValue}**")
        st.write(f"**Value of x2: {x2.varValue}**")
    else:
        st.error("No optimal solution found!")

# Instructions
st.write("Modify the coefficients and constraints in the sidebar, then click 'Solve Optimization Problem' to find the solution.")
