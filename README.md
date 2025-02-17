
# Inventory Manager

This project uses Django Rest Framework to provide api endpoints for a simple inventory management application


## API Reference

### Item Endpoints

#### Get all items

Endpoint for listing all items

```http
  GET 
```

To filter items by category use:

```http
  GET ?category=<str:id>
```
where id is the id of the category you want to filter by.

#### Get, update or delete item

Endpoint for retrieving an item, then updating or deleting it.

```http
  [GET,POST,DELETE] /item/<str:pk>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### Add new item

Endpoint for adding new item

```http
  POST /add-item/
```

### State Endpoints

#### Get all states

Endpoint for listing all item states

```http
  GET /states/
```

#### Add states

Endpoint for adding new item state

```http
  POST /add-state/
```

### Category Endpoints

#### Get, update or delete category

```http
   [GET,PUT,DELETE] /category/<str:pk>/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of category to fetch |

#### List categories
 
 Endpoint for listing all ategories

```http
  GET /categories/
```

#### Add category

```http
  POST /add-category/
```

### Tag Endpoints

#### List tags

Endpoint for listing all item tags

```http
  GET /tags/
```

#### Add tag

```http
  POST /add-tag/
```
