def employee_seniority_levels_query(employee_id: int):
    return f"""
      SELECT sl.id, sl.name, r.name as role_name, sl.description 
      FROM seniority_level sl
      JOIN seniority_level_skill sls ON sl.id = sls.seniority_level_id
      JOIN employee_skill es ON sls.skill_id = es.skill_id
      JOIN employee e ON es.employee_id = e.id
      JOIN role r ON sl.role_id = r.id
      WHERE es.employee_id = {employee_id} AND sl.role_id = e.role_id
      GROUP BY sl.id, sl.name, r.name
      HAVING COUNT(*) = (SELECT COUNT(*) FROM seniority_level_skill WHERE seniority_level_id = sl.id);
      """
