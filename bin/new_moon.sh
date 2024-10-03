
RESOURCE_NAME=$1
PLANET_NAME=$2

hugo new content --kind moon "locations/moons/${RESOURCE_NAME}.md"
DATA_FILE="data/moons/${RESOURCE_NAME}.yaml"

cat << EOF > "${DATA_FILE}"
name: ${RESOURCE_NAME}
planet: ${PLANET_NAME}
type: 
gravity: G
temperature: 
atmosphere: 
magnetosphere: 
water: 
o2_percent: TBD
surface_temp: TBD
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