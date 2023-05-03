## Data model 

### Tables 
    - appels_groupe_out 
    - operators 
    - groupes 
    - appels_group_out_durees 
    - appels_transferts

#### OutgroupCalls
    - id 
    - id_appel 
    - date 
    - service_num 
    - operator_id
    - operator_name 
    - operator_email 
    - group_id 
    - group_name 
    - ringing_duration 
    - waiting_duration 
    - communication_duration 
    - on_hold_duration 
    - catchup_duration
    - post_call_duration 

### Operator 
    - id 
    - name 
    - mail 

### Group 
    - id 
    - name 

### OutGroupCallDurations 
    - group_id 
    - call_id 

### Call
    - id 
    - operator_1 
    - operator_2 
    - caller_number 
    - receiver_number  
    - service_number 
    - service_id 


### CallTransfers


### Service 
    - id 
    - name 
    - 