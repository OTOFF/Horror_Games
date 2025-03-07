// Code By Meng Li
$(document).ready(function(){
    function clearForm() {
        $("#name-input").val("").focus();
        $("#image-input").val("");
        $("#intro-input").val("");
        $("#price-input").val("");
        $("#rate-input").val("");
        $("#system-input").val("");
    }

    $("#search-form").on("submit", function (event) {
        event.preventDefault();  

        let query = $("#search-input").val().trim(); 
        if (query === ""){
            $("#search-input").val("").focus();
            return;
        }; 
        let encodedQuery = encodeURIComponent(query)
        window.location.href = `/search?query=${encodedQuery}`;
        $("#search-input").val("").focus();
    });

    $("#reams_input").keypress(function(e){
        if(e.which === 13){
            $(".btn-outline-dark").click();
        }
    });
    $(document).on("click", ".search-item a", function (event) {
        event.preventDefault();
        let gameUrl = $(this).attr("href");
        window.location.href = gameUrl;
    });
    $("#add-btn").on("click", function(event){
        event.preventDefault();
        window.location.href = `/add`;
    })
    $("#add-game-form").on("submit", function(event){
        event.preventDefault();
    
        $("#name-warning").text(""); 
        $("#intro-warning").text(""); 
        $("#price-warning").text(""); 
        $("#image-warning").text(""); 
        $("#rate-warning").text(""); 
        $("#system-warning").text(""); 
        $(".is-invalid").removeClass("is-invalid");
    
        let name = $("#name-input").val().trim();
        let image = $("#image-input").val().trim();
        let introduction = $("#intro-input").val().trim();
        let price = $("#price-input").val().trim();
        let rate = $("#rate-input").val().trim();
        let supportive_system = $("#system-input").val().trim();
    
        let newGame = { name, image, introduction, price, rate, supportive_system };
    
        $.ajax({
            url: "/save_game",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify(newGame),
            success: function(response) {
                let gameId = response.game.id; 
                $("#success").html(`
                    <div class="alert alert-success alert-dismissible fade show" role="alert">
                        <strong>New item successfully created!</strong> 
                        <a href="/view/${gameId}" class="btn btn-success btn-sm ms-2">See it here</a>
                        <button class="btn btn-primary btn-sm ms-2" id="add-another">Add another</button>
                    </div>
                `);
                clearForm();

                // 让 "Add another" 按钮清空成功消息并继续添加新游戏
                $("#add-another").on("click", function(){
                    $("#success").html("");  // 移除成功消息
                    clearForm();
                });
            },
            error: function(xhr) {
                if (xhr.responseJSON && xhr.responseJSON.errors) {
                    let errors = xhr.responseJSON.errors;
                    if (errors.name) {
                        $("#name-warning").text(errors.name);
                        $("#name-input").addClass("is-invalid");
                    }
                    if (errors.image) {
                        $("#image-warning").text(errors.image);
                        $("#image-input").addClass("is-invalid");
                    }
                    if (errors.introduction) {
                        $("#intro-warning").text(errors.introduction);
                        $("#intro-input").addClass("is-invalid");
                    }
                    if (errors.price) {
                        $("#price-warning").text(errors.price);
                        $("#price-input").addClass("is-invalid");
                    }
                    if (errors.rate) {
                        $("#rate-warning").text(errors.rate);
                        $("#rate-input").addClass("is-invalid");
                    }
                    if (errors.supportive_system) {
                        $("#system-warning").text(errors.supportive_system);
                        $("#system-input").addClass("is-invalid");
                    }
                }
            }
        });
    });

    $("#edit-btn").on("click", function(event){
        event.preventDefault();
        let gameId = $(this).data("id");
        window.location.href = `/edit/${gameId}`;
    });

    $("#edit-form").on("submit", function (event) {
        event.preventDefault(); 
    
        $(".warning").text("");
        $(".is-invalid").removeClass("is-invalid");
    
        let gameId = $("#game-id").val().trim();
        let title = $("#title").val().trim();
        let image = $("#image").val().trim();
        let introduction = $("#introduction").val().trim();
        let price = $("#price").val().trim();
        let rate = $("#rate").val().trim();
    
        let supportive_system = $("#system").val().trim().split(",").map(s => s.trim()).filter(s => s !== "");
    
        let updatedGame = { title, image, introduction, price, rate, supportive_system };
    
        $.ajax({
                url: `/edit/${gameId}`,
                type: "POST",
                contentType: "application/json",
                data: JSON.stringify(updatedGame),
                success: function (response) {
                    window.location.href = `/view/${gameId}`; // 提交成功后跳转
                },
                error: function (xhr, status, error) {
                    console.error("Error updating game:", error);
                    alert("Failed to update game. Please try again.");
                }
        });
    });

    $("#dis-btn").on("click", function (event) {
        event.preventDefault(); 

        let confirmation = confirm("Are you sure you want to discard your changes?");
        if (confirmation) {
            let gameurl = $(this).attr("href");
            window.location.href = gameurl;
        }
    });
});