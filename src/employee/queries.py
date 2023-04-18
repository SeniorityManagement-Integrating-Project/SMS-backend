def employee_seniority_levels_query(employee_id: int):
    return f"""
    SELECT  sl.*, r.name AS role_name, MAX(es.attainment_date) AS attainment_date
    FROM employee e
    JOIN role r ON e.role_id = r.id
    JOIN seniority_level sl ON r.id = sl.role_id
    JOIN seniority_level_skill sls ON sl.id = sls.seniority_level_id
    JOIN employee_skill es ON e.id = es.employee_id AND sls.skill_id = es.skill_id
    WHERE e.id = {employee_id}
    GROUP BY r.name, sl.name, sl.description, sl.id
    HAVING COUNT(*) = (SELECT COUNT(*) FROM seniority_level_skill WHERE seniority_level_id = sl.id)
    """


def employee_current_seniority_level_query(employee_id: int):
    return employee_seniority_levels_query(employee_id) + "ORDER BY attainment_date DESC LIMIT 1"
