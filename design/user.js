
db.createCollection( 'user', {validator: {$jsonSchema: {bsonType: 'object',required: [         'username',          'email',          'hashed_password'],properties: {username: {bsonType: 'string'},email: {bsonType: 'string'},hashed_password: {bsonType: 'string'}}         }      }});  