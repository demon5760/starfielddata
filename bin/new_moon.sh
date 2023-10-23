
RESOURCE_NAME=$1
PLANET_NAME=$2

hugo new content --kind moon "locations/moons/${RESOURCE_NAME}.md"

cat << EOF > "data/moons/${RESOURCE_NAME}.yaml"
name: ${RESOURCE_NAME}
planet: ${PLANET_NAME}
type: 
gravity: G
temperature: 
atmosphere: 
magnetosphere: 
fauna_rating: 
flora_rating: 
water: 
o2: 
temp: 
flora: {}
fauna: {}
traits:
  - TBD
resources:
  - TBD
credits:
  - TBD
EOF