import plotly.graph_objects as go

def generate_visits_chart():
    """Generates a Plotly chart of student visits."""
    with app.app_context():
        # Get the count of visits per student
        visits_data = db.session.query(Student.name, func.count(Visit.id).label('visit_count')) \
            .join(Visit, Student.id == Visit.student_id) \
            .group_by(Student.name) \
            .order_by(desc('visit_count')) \
            .all()

        # Separate student names and visit counts for Plotly
        student_names = [row.name for row in visits_data]
        visit_counts = [row.visit_count for row in visits_data]

        # Create a bar chart
        fig = go.Figure(data=[go.Bar(x=student_names, y=visit_counts)])
        fig.update_layout(
            title='Student Visits',
            xaxis_title='Student Name',
            yaxis_title='Number of Visits'
        )
        return fig.to_html(full_html=False)