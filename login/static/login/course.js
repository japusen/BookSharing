$(document).ready(function() {
    $('#bookTable').dataTable({
    	paging: true,
    	pagingType: "simple_numbers",
    	lengthChange: false,
        searching: false,
    	ordering:  false,
        info:     false,
    });

    $("#bookForm").submit(function(event){
    	//prevent submit
    	event.preventDefault();
    	//send data
    	$.post("/addBook/", $("#bookForm").serialize(), function(data) {
    		//close modal
    		if(data.success === "pass")
    		{
    			$('#myModal').modal('hide');
    			console.log("it worked");
    		}
    		else
    			console.log("something is wrong");
    	});
    	
	});
});

