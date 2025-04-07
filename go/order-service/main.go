package main

import (
	"github.com/gofiber/fiber/v2"
	"github.com/google/uuid"
)

type Order struct {
	ID          string  `json:"id"`
	UserID      string  `json:"user_id"`
	ProductID   string  `json:"product_id"`
	Quantity    int     `json:"quantity"`
	TotalAmount float64 `json:"total_amount"`
	Status      string  `json:"status"`
}

var orders []Order

func main() {
	app := fiber.New()

	app.Get("/", func(c *fiber.Ctx) error {
		return c.JSON(fiber.Map{
			"message": "Order Service is running",
		})
	})

	app.Post("/orders", createOrder)
	app.Get("/orders", getOrders)
	app.Get("/orders/:id", getOrder)
	app.Put("/orders/:id", updateOrder)
	app.Delete("/orders/:id", deleteOrder)

	app.Listen(":3000")
}

func createOrder(c *fiber.Ctx) error {
	var order Order
	if err := c.BodyParser(&order); err != nil {
		return c.Status(400).JSON(fiber.Map{"error": "Cannot parse JSON"})
	}

	order.ID = uuid.New().String()
	orders = append(orders, order)
	return c.Status(201).JSON(order)
}

func getOrders(c *fiber.Ctx) error {
	return c.JSON(orders)
}

func getOrder(c *fiber.Ctx) error {
	id := c.Params("id")
	for _, order := range orders {
		if order.ID == id {
			return c.JSON(order)
		}
	}
	return c.Status(404).JSON(fiber.Map{"error": "Order not found"})
}

func updateOrder(c *fiber.Ctx) error {
	id := c.Params("id")
	var updatedOrder Order
	if err := c.BodyParser(&updatedOrder); err != nil {
		return c.Status(400).JSON(fiber.Map{"error": "Cannot parse JSON"})
	}

	for i, order := range orders {
		if order.ID == id {
			updatedOrder.ID = id
			orders[i] = updatedOrder
			return c.JSON(updatedOrder)
		}
	}
	return c.Status(404).JSON(fiber.Map{"error": "Order not found"})
}

func deleteOrder(c *fiber.Ctx) error {
	id := c.Params("id")
	for i, order := range orders {
		if order.ID == id {
			orders = append(orders[:i], orders[i+1:]...)
			return c.JSON(fiber.Map{"message": "Order deleted successfully"})
		}
	}
	return c.Status(404).JSON(fiber.Map{"error": "Order not found"})
}
