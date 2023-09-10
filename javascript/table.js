async function getData() {
    const response = await fetch('https://raw.githubusercontent.com/fedegonzal/ista-test/main/data/data.json');
    const data = await response.json();
    return data;
}

getData().then(data => {

    const template = document.getElementById("rowTemplate");
    const table = document.getElementById("table");
    const tbody = table.querySelector('tbody');

    data.forEach(element => {
        let clone = template.cloneNode(true);

        clone.getElementsByClassName("id")[0].textContent = element.id;
        clone.getElementsByClassName("university")[0].textContent = element.university;
        clone.getElementsByClassName("country")[0].textContent = element.country;

        if (element.location == null) {
            element.location = {
                lat: 0,
                lng: 0
            };
        }
        let gmapsUrl = "https://www.google.com/maps?q=" + element.location.lat + "," + element.location.lng;
        let gmapsRef = "<a href='" + gmapsUrl + "' target='_blank'>open location</a>";

        clone.getElementsByClassName("location")[0].innerHTML = gmapsRef;
        clone.id = element.id;
        clone.style = null;

        tbody.appendChild(clone);
    });

    let dtable = new DataTable('#table', {
        fixedHeader: true,
        paging: false,
        searching: false,
    });

});
