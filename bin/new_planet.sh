
RESOURCE_NAME=$1
SYSTEM_NAME=$2

hugo new content --kind planet "locations/planets/${RESOURCE_NAME}.md"

cat << EOF > "data/planets/${RESOURCE_NAME}.yaml"
name: ${RESOURCE_NAME}
system: ${SYSTEM_NAME}
type: 
gravity: G
temperature: 
atmosphere: 
magnetosphere: 
fauna_rating: 
flora_rating: 
water: 
o2: %
temp: ° 
flora: {}
fauna: {}
traits:
  - TBD
resources:
  - TBD
credits:
  - TBD
EOF