$(document).ready(function () {
    const csrfToken = document.cookie.split('; ')
        .find(row => row.startsWith('csrftoken='))?.split('=')[1] || '';

    function loadSubscribers() {
        $.get("/subscribers/list", function (data) {
            let rows = "";
            data.forEach(sub => {
                rows += `<tr>
                            <td>${sub.first_name || "-"}</td>
                            <td>${sub.last_name || "-"}</td>
                            <td>${sub.email}</td>
                            <td>${sub.birthday || "-"}</td>
                         </tr>`;
            });
            $("#subscribersTable").html(rows);
        });
    }

    $("#subscriberForm").on("submit", function (event) {
        event.preventDefault();
        let formData = $(this).serialize();

        $.ajax({
            type: "POST",
            url: "/subscribers/add",
            data: formData,
            headers: { "X-CSRFToken": csrfToken },
            success: function (response) {
                if (response.status === "success") {
                    alert("Подписчик добавлен!");
                    $("#subscriberForm")[0].reset();
                    loadSubscribers();
                } else {
                    alert("Ошибка: " + JSON.stringify(response.errors));
                }
            },
            error: function (xhr) {
                alert(`Ошибка ${xhr.status}: ${xhr.statusText}`);
            }
        });
    });

    loadSubscribers();
});
