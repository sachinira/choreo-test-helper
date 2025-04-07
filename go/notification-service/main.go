package main

import (
	"github.com/gofiber/fiber/v2"
	"github.com/google/uuid"
)

type Notification struct {
	ID        string `json:"id"`
	UserID    string `json:"user_id"`
	Type      string `json:"type"`
	Message   string `json:"message"`
	Read      bool   `json:"read"`
	Timestamp string `json:"timestamp"`
}

var notifications []Notification

func main() {
	app := fiber.New()

	app.Get("/", func(c *fiber.Ctx) error {
		return c.JSON(fiber.Map{
			"message": "Notification Service is running",
		})
	})

	app.Post("/notifications", createNotification)
	app.Get("/notifications", getNotifications)
	app.Get("/notifications/:id", getNotification)
	app.Get("/notifications/user/:user_id", getNotificationsByUser)
	app.Put("/notifications/:id/read", markAsRead)

	app.Listen(":3002")
}

func createNotification(c *fiber.Ctx) error {
	var notification Notification
	if err := c.BodyParser(&notification); err != nil {
		return c.Status(400).JSON(fiber.Map{"error": "Cannot parse JSON"})
	}

	notification.ID = uuid.New().String()
	notification.Read = false
	notifications = append(notifications, notification)
	return c.Status(201).JSON(notification)
}

func getNotifications(c *fiber.Ctx) error {
	return c.JSON(notifications)
}

func getNotification(c *fiber.Ctx) error {
	id := c.Params("id")
	for _, notification := range notifications {
		if notification.ID == id {
			return c.JSON(notification)
		}
	}
	return c.Status(404).JSON(fiber.Map{"error": "Notification not found"})
}

func getNotificationsByUser(c *fiber.Ctx) error {
	userID := c.Params("user_id")
	var userNotifications []Notification
	for _, notification := range notifications {
		if notification.UserID == userID {
			userNotifications = append(userNotifications, notification)
		}
	}
	return c.JSON(userNotifications)
}

func markAsRead(c *fiber.Ctx) error {
	id := c.Params("id")
	for i, notification := range notifications {
		if notification.ID == id {
			notifications[i].Read = true
			return c.JSON(notifications[i])
		}
	}
	return c.Status(404).JSON(fiber.Map{"error": "Notification not found"})
}
