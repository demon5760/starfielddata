
RESOURCE_NAME=$1

hugo new content --kind resource "items/resources/${RESOURCE_NAME}.md"

cat << EOF > "data/resources/${RESOURCE_NAME}.yaml"
name: ${RESOURCE_NAME}
type: Organic
rarity: 
mass: 
value: 
farming:
  Greenhouse:
    Water: 1
  Animal Husbandry Facility:
    - Fiber: 2
      Water: 1
    - Nutrient: 2
      Water: 1
credits:
  - TBD
EOF