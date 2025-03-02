package com.example.todo.controller;

import com.example.todo.model.Todo;
import com.example.todo.repository.TodoRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/todos")
public class TodoController {

    @Autowired
    private TodoRepository repository;

    @PostMapping
    public Todo create(@RequestBody Todo todo) {
        return repository.save(todo);
    }

    @GetMapping
    public List<Todo> getAll() {
        return repository.findAll();
    }
}