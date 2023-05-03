# api-communication

## SQL Request 

```sql
Select ago.id, ago.id_appel as "id_appel", ago.dt as "date" ,ago.service_num , ago.id_op as "operator.id",  o.realname as "operator.name", o.email as "operator.mail" , ago.id_groupe as "group.id", g.nom as "group.name", ago.duree_sonnerie as "ringing_duration", ago.duree_attente as "waiting_duration" , ago.duree as "communication_duration", agod.about_pause  as "on_hold_duration", agod.catchup as "catchup_duration" , agod.ppa as "post_call_duration", at2.id as "transfer.id"
from appels_groupe_out as ago
INNER  JOIN appels_groupe_out ag on ag.id_client = 176147 and ag.dt > "2023-01-25 00:00:00" and ag.dt < "2023-01-27 23:59:59" and ag.id = ago.id
INNER JOIN operateurs as o on o.id = ago.id_op
LEFT JOIN groupes g as on g.id = ago.id_groupe
LEFT JOIN appels_groupe_out_durees agod as on agod.id_appels_groupe_out = ago.id
LEFT JOIN appels_transferts as at2 on at2.id_init_appels_groupe_out = ago.id
```

## JSON API

```json
{					
	app: "api-v2",				
	version: "preprod",				
	datetime: "2022-09-28T09:47:54.792743",				
	timestamp: "1664351274.792743",				
	code: 200,				
	status: "success",				
	data: {				
		limit: 1000,			
		page: 1,			
		pages: 11,			
		elements: 10372,			
		communications_details_operator: [			
			{		
			id: 1,		
			id_appel: 2,		
			date: "2022-08-01T08:35:28",		
			service_num: 33,		
			operator.id: 25,		
			operator.name: "tom",		
			operator.email: "thikari@gihtub.com",		
			group.id: 123,		
			group.name: "SA",		
			waiting_duration: 24,		
			communication_duration: 587,		
			on_hold_duration: 18,		
			ringing_duration: 2,		
			catchup_duration: 15,		
			post_call_duration: 71,		
			transfer_id: 4564		
			}		
		]			
	}				
}		
```			


# TODO
1. Create a database and connect to your backend
2. Build an api to serve this data as describe
3. Write unit test check if the api data structure is the same as described
4. Write postman test

# Requirement
1. Use a type language
2. use JWT as authentification
3. use clean code principles
4. respect json type 

May our code be good :)
