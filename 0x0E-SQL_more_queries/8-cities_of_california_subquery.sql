-- Lists all cities of California that can be foung in 'hbtn_0d_usa'
-- Results should be sorted in ascending order by 'cities.id'
SELECT `id`, `name`
	FROM `cities`
WHERE `state_id` IN
	( SELECT `id`
		FROM `states`
	  WHERE `name` = "California")
ORDER BY `id`;
