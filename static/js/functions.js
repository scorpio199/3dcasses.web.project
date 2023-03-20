function ReplaceNumberWithCommas(yourNumber) {
    //Seperates the components of the number
    var n= yourNumber.toString().split(".");
    //Comma-fies the first part
    n[0] = n[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    //Combines the two sections
    return n.join(".");
}

var url_api = 'http://localhost:8000/shopaccount/'

function get_list_marketplace(){
    $('#table-marketplace').DataTable({
        columnDefs: [{
            targets: -1,
            data: null
        }],
        ajax: {
          url: url_api+'list_marketplace/',
          dataSrc: function(json) {
            var data = [];

            // Iterate over each object in the JSON response and create a new array of arrays
            $.each(json.dataset, function(index, e) {
                index++
                data.push([index, e.id, e.mp_name]);
            });

            return data;
          }
        },
        columns: [
            { title: 'No' },
            { title: 'ID', visible: false },
            { title: 'Marketplace',                           
                render: function(data, type, row, meta) {
                    return '<a href="../detail_view/'+row[1]+'/1" class="link">'+data+'</a>';
                } 
            },
            { title: 'Action',
                render: function(data, type, row, meta) {
                    return '<a href="../update_view/'+row[1]+'/1" class="link">Edit</a>';
                } 
            }
        ],
        paging: false,
        info: false
    });
}

function get_list_transaction(date_from, date_to){
	if (date_from == ''){
		date_from = '-'
	}

	if (date_to == ''){
		date_to = '-'
	}
	
	$('#table-transaction').DataTable({
        columnDefs: [{
            targets: -1,
            data: null
        }],
        ajax: {
          url: url_api+'list_transaction/'+date_from+'/'+date_to,
          dataSrc: function(json) {
            var data = [];

            // Iterate over each object in the JSON response and create a new array of arrays
            $.each(json.dataset, function(index, e) {
                index++
                data.push([index, e.id, e.date, e.mp_id.mp_name, 
                        e.order_id, e.product_name, e.product_category, e.quantity,
                        ReplaceNumberWithCommas(e.selling_price), ReplaceNumberWithCommas(e.basic_price)]);
            });

            return data;
          }
        },
        columns: [
            { title: 'No' },
            { title: 'ID', visible: false },
            { title: 'Date' },
            { title: 'Marketplace' },                          
            { title: 'Order ID',
                render: function(data, type, row, meta) {
                    return '<a href="../detail_view/'+row[1]+'/2" class="link">'+data+'</a>';
                } 
            },
            { title: 'Product name' },
            { title: 'Category' },
            { title: 'Quantity' },
            { title: 'Selling price' },
            { title: 'Basic price' },
            { title: 'Action',
                render: function(data, type, row, meta) {
                    return '<a href="../update_view/'+row[1]+'/2" class="link">Edit</a>';
                } 
            }
        ],
        pagingType: 'full_numbers',
        pageLength: 25,
        order: [[0, 'desc']]
    });
}


function get_list_detail_transaction(date_from, date_to){
	let data_id = $('#data_id').val()
	let data_no = $('#data_no').val()

	if (date_from == ''){
		date_from = '-'
	}

	if (date_to == ''){
		date_to = '-'
	}

	let url_list_detail = url_api+'list_detail/'+data_id+'/'+data_no+'/'+date_from+'/'+date_to

	if (data_no == 1){     		
    	$('#table-detail-tr').DataTable({
            columnDefs: [{
                data: null
            }],
            ajax: {
              url: url_list_detail,
              dataSrc: function(json) {
                let data = [];
                let e = json.marketplace

                $('.mp_id').text(e.id)
                $('.mp_name').text(e.mp_name)
                $('.total_qty_order').html('<b>'+json.total_qty+'</b>')
                $('.total_selling_price').html('<b>'+ReplaceNumberWithCommas(json.total_selling_price)+'</b>')
                $('.total_basic_price').html('<b>'+ReplaceNumberWithCommas(json.total_basic_price)+'</b>')
                $('.total_profit').html('<b>'+ReplaceNumberWithCommas(json.total_profit)+'</b>')

                // Iterate over each object in the JSON response and create a new array of arrays
                $.each(json.transaction, function(index, e) {
                    index++
                    data.push([index, e.date,  
                            e.order_id, e.product_name, e.product_category, e.quantity,
                            ReplaceNumberWithCommas(e.selling_price), ReplaceNumberWithCommas(e.basic_price), ReplaceNumberWithCommas(e.profit), e.margin]);
                });

                return data;
              }
            },
            columns: [
                { title: 'No' },
                { title: 'Date' },                          
                { title: 'Order ID' },
                { title: 'Product name' },
                { title: 'Category' },
                { title: 'Quantity' },
                { title: 'Nett Selling price' },
                { title: 'Basic price' },
                { title: 'Profit' },
                { title: 'Margin',
                	render: function(data, type, row, meta) {
                        return data+' %';
                    } 
                }
            ],
            pagingType: 'full_numbers',
            pageLength: 25,
            dom: 'Bfrtip',
	        buttons: [
	            'copy',
	            {
	                extend: 'csv',
	                exportOptions: {
	                    columns: [ 0, 1, 2, 3, 4, 5, 6, 7 ]
	                }
	            },
	            'excel', 'pdf', 'print'
	        ]
        });
	}else if (data_no == 2){
		$.get(url_list_detail, function(data, status){
			let e = data.transaction
			$('.tr_id').text(e.id)
			$('.tr_mp_id').text(e.mp_id.mp_name)
			$('.order_id').text(e.order_id)
			$('.product_name').text(e.product_name)
			$('.product_category').text(e.product_category)
			$('.quantity').text(e.quantity)
			$('.selling_price').text(ReplaceNumberWithCommas(e.selling_price))
			$('.basic_price').text(ReplaceNumberWithCommas(e.basic_price))
			$('.profit').text(ReplaceNumberWithCommas(e.profit))
			$('.notes').text(e.notes)
		});
	}else{
		console.log('')
	}
}

function get_list_payout_type() {
	$('#table-payout-type').DataTable({
        columnDefs: [{
            targets: -1,
            data: null
        }],
        ajax: {
          url: url_api+'list_payout_type/',
          dataSrc: function(json) {
            var data = [];

            // Iterate over each object in the JSON response and create a new array of arrays
            $.each(json.dataset, function(index, e) {
                index++
                data.push([index, e.id, e.pay_type_name, e.pay_type_perc]);
            });

            return data;
          }
        },
        columns: [
            { title: 'No' },
            { title: 'ID', visible: false },
            { title: 'Type Category',
            	render: function(data, type, row, meta) {
                    return '<a href="../detail_view/'+row[1]+'/3" class="link">'+data+'</a>';
                } 
            },                          
            { title: 'Percentage',
                render: function(data, type, row, meta) {
                    return data+' %';
                } 
            },
            { title: 'Action',
                render: function(data, type, row, meta) {
                    return '<a href="../update_view/'+row[1]+'/3" class="link">Edit</a>';
                } 
            }
        ],
        paging: false,
        info: false
    })
}

function get_list_payout(){
	$('#table-payout').DataTable({
        columnDefs: [{
            targets: -1,
            data: null
        }],
        ajax: {
          url: url_api+'list_payout/',
          dataSrc: function(json) {
          	var data = [];

            // Iterate over each object in the JSON response and create a new array of arrays
            $.each(json.dataset, function(index, e) {
                index++
                data.push([index, e.id, e.pay_date, e.pay_name, e.pay_type_id.pay_type_name, 
                        ReplaceNumberWithCommas(e.pay_value)]);
            });

            return data;
          }
        },
        columns: [
            { title: 'No' },
            { title: 'ID', visible: false },
            { title: 'Date' },
            { title: 'Payout Name' },                          
            { title: 'Payout Type' },
            { title: 'Payout Value' },
            { title: 'Action',
                render: function(data, type, row, meta) {
                    return '<a href="../update_view/'+row[1]+'/4" class="link">Edit</a>';
                } 
            }
        ],
        pagingType: 'full_numbers',
        pageLength: 25,
        order: [[0, 'desc']]
    });
}

function get_list_detail_payout(date_from, date_to){
	let data_id = $('#data_id').val()
	let data_no = $('#data_no').val()

	if (date_from == ''){
		date_from = '-'
	}

	if (date_to == ''){
		date_to = '-'
	}

	let url_list_detail = url_api+'list_detail/'+data_id+'/'+data_no+'/'+date_from+'/'+date_to
	
	$('#table-detail-p').DataTable({
        columnDefs: [{
            data: null
        }],
        ajax: {
          url: url_list_detail,
          dataSrc: function(json) {
            let data = [];
            let e = json.payout_type

            $('.pay_type_id').text(e.id)
            $('.pay_type_name').text(e.pay_type_name)
            $('.pay_type_perc').text(e.pay_type_perc)
            $('.total_payout').html('<b>'+ReplaceNumberWithCommas(json.total_payout)+'</b>')

            // Iterate over each object in the JSON response and create a new array of arrays
            $.each(json.payout, function(index, e) {
                index++
                data.push([index, e.pay_date, e.pay_name, ReplaceNumberWithCommas(e.pay_value)]);
            });

            return data;
          }
        },
        columns: [
            { title: 'No' },
            { title: 'Date' },    
            { title: 'Payout Name' },
            { title: 'Payout Value' }
        ],
        pagingType: 'full_numbers',
        pageLength: 25,
        dom: 'Bfrtip',
        buttons: [
            'copy', 'csv', 'excel', 'pdf', 'print'
        ]
    });
}

function filter_by_date(data){
	if (data == 'tr'){
		let start_date =  $('#tr_date_from').val()
        let end_date = $('#tr_date_to').val()

        table = $('#table-transaction').DataTable();
		table.destroy();
        get_list_transaction(start_date, end_date)
	}else if (data == 'tr-detail'){    			
    	let start_date =  $('#date_from').val()
        let end_date = $('#date_to').val()

        table = $('#table-detail-tr').DataTable();
		table.destroy();
        get_list_detail_transaction(start_date, end_date)
	}else{
		let start_date =  $('#pay_date_from').val()
        let end_date = $('#pay_date_to').val()

        table = $('#table-detail-p').DataTable();
		table.destroy();
        get_list_detail_payout(start_date, end_date)
	}
}

$(document).ready(function(){
	$('.accordion-content').hide();
	$('.widget-accordion').find('.accordion-toggle').click(function() {
		$('.accordion-toggle').each(function(){
	  	$(this).removeClass("opened");
	  });
	  // State change visuals
	  $(this).toggleClass('opened');

	  //Expand or collapse this panel
	  $(this).next().slideToggle('fast');

	  //Hide the other panels
	  $(".accordion-content").not($(this).next()).slideUp('fast');
	});

    try {
        // Your code goes here
        // This code might throw an error
        // If an error occurs, it will be caught by the catch block
        get_list_marketplace()
        get_list_transaction('-','-')
        get_list_detail_transaction('-','-')
        get_list_payout_type()
        get_list_payout()
        get_list_detail_payout('-','-')
    } catch (error) {
        console.log('An error occurred: ' + error.message);
        // Handle the error here
    }
})