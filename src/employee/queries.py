def employee_seniority_levels_query(employee_id: int):
    return f"""
        WITH required_skills AS (
            SELECT rsl.id AS role_seniority_level_id, COUNT(*) AS required_skill_count
            FROM role_seniority_level rsl
            JOIN seniority_level_skill sls ON rsl.id = sls.role_seniority_level_id
            GROUP BY rsl.id
        ),
        approved_skills AS (
            SELECT rsl.id AS role_seniority_level_id, COUNT(*) AS approved_skill_count, MAX(svr.updated_at) AS attainment_date
            FROM employee e
            JOIN role_seniority_level rsl ON e.role_id = rsl.role_id
            JOIN seniority_level_skill sls ON rsl.id = sls.role_seniority_level_id
            JOIN skill_validation_request svr ON e.id = svr.employee_id AND sls.skill_id = svr.skill_id AND svr.approved = true
            WHERE e.id = {employee_id}
            GROUP BY rsl.id
        )
        SELECT rsl.id, sl.level, sl.name as seniority_level_name , r.name as role_name, rsl.description, aps.attainment_date
        FROM employee e
        JOIN role_seniority_level rsl ON e.role_id = rsl.role_id
        JOIN role r ON r.id = e.role_id
        JOIN seniority_level sl ON rsl.seniority_level_id = sl.id
        JOIN required_skills rs ON rsl.id = rs.role_seniority_level_id
        JOIN approved_skills aps ON rsl.id = aps.role_seniority_level_id AND rs.required_skill_count = aps.approved_skill_count
        WHERE e.id = {employee_id}
    """


def employee_current_seniority_level_query(employee_id: int):
    return employee_seniority_levels_query(employee_id) + "ORDER BY sl.level DESC LIMIT 1"
