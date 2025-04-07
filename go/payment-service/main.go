package main

import (
	"github.com/gofiber/fiber/v2"
	"github.com/google/uuid"
)

type Payment struct {
	ID        string  `json:"id"`
	OrderID   string  `json:"order_id"`
	Amount    float64 `json:"amount"`
	Status    string  `json:"status"`
	Method    string  `json:"method"`
	Timestamp string  `json:"timestamp"`
}

var payments []Payment

func main() {
	app := fiber.New()

	app.Get("/", func(c *fiber.Ctx) error {
		return c.JSON(fiber.Map{
			"message": "Payment Service is running",
		})
	})

	app.Post("/payments", createPayment)
	app.Get("/payments", getPayments)
	app.Get("/payments/:id", getPayment)
	app.Get("/payments/order/:order_id", getPaymentsByOrder)

	app.Listen(":3001")
}

func createPayment(c *fiber.Ctx) error {
	var payment Payment
	if err := c.BodyParser(&payment); err != nil {
		return c.Status(400).JSON(fiber.Map{"error": "Cannot parse JSON"})
	}

	payment.ID = uuid.New().String()
	payments = append(payments, payment)
	return c.Status(201).JSON(payment)
}

func getPayments(c *fiber.Ctx) error {
	return c.JSON(payments)
}

func getPayment(c *fiber.Ctx) error {
	id := c.Params("id")
	for _, payment := range payments {
		if payment.ID == id {
			return c.JSON(payment)
		}
	}
	return c.Status(404).JSON(fiber.Map{"error": "Payment not found"})
}

func getPaymentsByOrder(c *fiber.Ctx) error {
	orderID := c.Params("order_id")
	var orderPayments []Payment
	for _, payment := range payments {
		if payment.OrderID == orderID {
			orderPayments = append(orderPayments, payment)
		}
	}
	return c.JSON(orderPayments)
}
