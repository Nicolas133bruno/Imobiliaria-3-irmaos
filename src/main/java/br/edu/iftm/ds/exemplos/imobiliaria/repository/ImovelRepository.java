package br.edu.iftm.ds.exemplos.imobiliaria.repository;

import br.edu.iftm.ds.exemplos.imobiliaria.domain.Imovel;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ImovelRepository extends JpaRepository<Imovel, Integer> { }
