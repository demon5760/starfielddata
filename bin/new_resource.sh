
RESOURCE_NAME=$1

hugo new content --kind resource "items/resources/${RESOURCE_NAME}.md"

cat << EOF > "data/resources/${RESOURCE_NAME}.yaml"
name: ${RESOURCE_NAME}
type: Manufactured
rarity: Rare
mass: 
value: 
crafting:
  Industrial Workbench:
    - TBD: 1
      TBD2: 1
      TBD3: 1
      TBD4: 1
  Simple Fabricator:
    - Aluminum: 1
      Iron: 1
credits:
  - Demon5760
EOF