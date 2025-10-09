package br.edu.iftm.ds.exemplos.imobiliaria.dto;

public class AuthResponse {
    private String token;

    public AuthResponse(String token) { this.token = token; }

    public String getToken() { return token; }
    public void setToken(String token) { this.token = token; }
}
