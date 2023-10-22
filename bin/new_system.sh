
RESOURCE_NAME=$1

hugo new content --kind system "locations/systems/${RESOURCE_NAME}.md"

cat << EOF > "data/systems/${RESOURCE_NAME}.yaml"
name: ${RESOURCE_NAME}
level: 
faction: None
catalogue_id: 
spectral_class: 
temperature: 
mass: 
radius: 
magnitude: 
planets: 
moons: 
credits:
  - Inara
EOF