function searchDogBreeds() {
    const searchInput = document.getElementById("searchInput").value.trim();

    if (searchInput === "") {
        alert("Por favor ingrese el nombre de una raza de perro.");
        return;
    }

    const apiUrl = `https://api.thedogapi.com/v1/breeds/search?q=${searchInput}`;

    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            if (data.length === 0) {
                document.getElementById("results").innerHTML = "No se encontraron razas de perro.";
            } else {
                const resultsDiv = document.getElementById("results");
                resultsDiv.innerHTML = "";

                data.forEach(breed => {
                    const breedDiv = document.createElement("div");
                    breedDiv.textContent = breed.name;
                    resultsDiv.appendChild(breedDiv);

                  
                    const imageUrl = `https://api.thedogapi.com/v1/images/search?breed_ids=${breed.id}`;
                    fetch(imageUrl)
                        .then(response => response.json())
                        .then(images => {
                            if (images && images.length > 0) {
                                const imageSrc = images[0].url;
                                const img = document.createElement("img");
                                img.src = imageSrc;
                                breedDiv.appendChild(img);
                            }
                        })
                        .catch(error => {
                            console.error("Error al buscar imagen de raza de perro:", error);
                        });
                });
            }
        })
        .catch(error => {
            console.error("Error al buscar razas de perro:", error);
            document.getElementById("results").innerHTML = "Se produjo un error al buscar las razas de perro.";
        });
}
