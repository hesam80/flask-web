//JSON JSONIFY JSON.stringify(products)  
//Objects and destructuring
const oneproductobj={title:'film',price:99,exist:true}
const products=[
{
id:1,
title: 'Book 1',
price: 99,
exist: true,
},
{
    id:2,
    title: 'Book 2',
    price: 89,
    exist: false,
    },
    {
        id:3,
        title: 'Book 3',
        price: 79,
        exist: true,
        },


]
//vaghti object ro mikhahim befrstim be platform python
const data= JSON.stringify(products);

//vaghti reshte string miad va tabdilesh konim be object
const responce= JSON.parse(data)



console.log("hello");
console.log(products);
console.log(data);
console.log(title);

