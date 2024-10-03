
RESOURCE_NAME=$1
SYSTEM_NAME=$2

hugo new content --kind planet "locations/planets/${RESOURCE_NAME}.md"
DATA_FILE="data/planets/${RESOURCE_NAME}.yaml"

cat << EOF > "${DATA_FILE}"
name: ${RESOURCE_NAME}
system: ${SYSTEM_NAME}
type: 
gravity: G
temperature: 
o2_percent: TBD
surface_temp: TBD
water: 
o2_percent: 
surface_temp: 
fauna: {}
fauna_rating: 
flora: {}
flora_rating: 
traits: []
resources: []
credits:
  - Demon5760
EOF

code "${DATA_FILE}"